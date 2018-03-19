## Pipeable Object Classes ##

class AbstractPipeFunction:
    def __init__(self, function, *arguments, **keywords):
        self.function = function
        self.arguments = arguments
        self.keywords = keywords

    def __rrshift__(self, other):
        return self(other)

class PipeFunction(AbstractPipeFunction):
    def __call__(self, operand):
        return self.function(operand, *self.arguments, **self.keywords)

class PartialPipeFunction(AbstractPipeFunction):
    def __call__(self, operand):
        placeholder = ____  
        placeholder_in_arguments = placeholder in self.arguments
        placeholder_in_keywords  = placeholder in self.keywords.values()
        placeholder_in_call = placeholder_in_arguments or placeholder_in_keywords

        if placeholder_in_arguments:
            arguments = [operand if a==placeholder else a for a in self.arguments]
        else:
            arguments = self.arguments

        if placeholder_in_keywords:   
            keywords = { k:operand if v==placeholder else v for (k,v) in self.keywords.items() }
        else:
            keywords = self.keywords
        
        if placeholder_in_call:
            return self.function(*arguments, **keywords)
        else:
            return self.function(operand, *arguments, **keywords)

        

## Identifier Chain Processor Classes ##

import inspect

class AbstractIdentifierCatcher:
    def __init__(self, _identifier_chain=None, scope=None):
        if _identifier_chain:
            self._identifier_chain = _identifier_chain
        elif scope:
            self._identifier_chain = __import__(scope)
        else:
            caller_frame = inspect.currentframe().f_back
            detected_module_name = caller_frame.f_globals.get("__name__", "<unknown module>")
            self._identifier_chain = __import__(detected_module_name)

    def __getattr__(self, name):
        return self.__class__( getattr(self._identifier_chain, name) )

    def __rrshift__(self, other):
        return self()(other)

class FunctionCatcher(AbstractIdentifierCatcher):
    def __call__(self, *arguments, **keywords):
        return PipeFunction(self._identifier_chain, *arguments, **keywords)

class PartialCatcher(AbstractIdentifierCatcher):
    def __call__(self, *arguments, **keywords):
        return PartialPipeFunction(self._identifier_chain, *arguments, **keywords)

## Placeholders ##

class InputPlaceholder: pass

## Interface ##

____ = InputPlaceholder()

# class MethodCatcher:
#     def __init__(self, scope=[]):
#         self._scope = scope

#     def __getattr__(self, name):
#         new_scope = [*self._scope, name]
#         return MethodCatcher(scope=new_scope)

#     def invoke_on(self, other):
#         def resolve_identifier_chain(root_object, chain):
#                 if len(chain) == 1:
#                     return getattr(root_object, chain[0])
#                 else:
#                     head = chain[0]
#                     tail = chain[1:]
#                     sub_object = getattr(root_object, head)
#                     return resolve_identifier_chain(sub_object, tail)

#         return resolve_identifier_chain(other, self._scope)

def invoke_deffered_chain(input_object, chain):
    if len(chain) == 1:
        return chain[0].invoke_on(input_object)
    else:
        head = chain[0]
        tail = chain[1:]
        sub_object = head.invoke_on(input_object)
        return invoke_deffered_chain(sub_object, tail)

class DefferredAttribute:
    def __init__(self, attribute_name):
        self.attribute_name = attribute_name

    def invoke_on(self, input):
        return getattr(input, self.attribute_name)

    def __repr__(self):
        return f"DefferredAttribute: .{self.attribute_name}"

class DefferredMethodCall:
    def __init__(self, *arguments, **keywords):
        self.arguments = arguments
        self.keywords = keywords

    def invoke_on(self, input):
        return input(*self.arguments, **self.keywords)

    def __repr__(self):
        return f"DefferredMethodCall: {self.arguments} {self.keywords}"

class DefferredSubscript:
    def __init__(self, key):
        self.key = key

    def invoke_on(self, input):
        return input.__getitem__(self.key)

    def __repr__(self):
        return f"DefferredSubscript: {self.key}"

class ChainCatcher:
    def __init__(self, chain=[]):
        self._chain = chain

    def __add_link__(self, new_link):
        new_chain = [*self._chain, new_link]
        return ChainCatcher(chain = new_chain)

    def __getattr__(self, attribute):
        return self.__add_link__( DefferredAttribute(attribute) )

    def __getitem__(self, key):
        return self.__add_link__( DefferredSubscript(key) )

    def __call__(self, *args, **kwargs):
        return self.__add_link__( DefferredMethodCall(*args, **kwargs) )

    def __repr__(self):
        return f"ChainCatcher: {self._chain}"

class MethodCatcher:
    def __init__(self, scope=None):
        self._identifier = scope

    def __getattr__(self, name):
        return MethodCatcher(scope=name)

    def invoke_on(self, root_object):
        return getattr(root_object, self._identifier)

# class DeferredMethodAccessor:
    # def execute():
    #     precursor_result = self._precursor.invoke_on(root_object)


#     def invoke_on(self, root_object):
#         if self._prerequisite:
#             self._prerequisite.invoke_on(root_object)
#         else:

# class DeferredSubscriptAccessor:
#     def invoke_on(self, root_object):
#         if self._prerequisite:
#             self._prerequisite.invoke_on(root_object)
#         else:

