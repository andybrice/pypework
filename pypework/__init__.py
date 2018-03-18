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

class MethodCatcher:
    def __init__(self, scope=[]):
        self._scope = scope

    def __getattr__(self, name):
        new_scope = [*self._scope, name]
        return MethodCatcher(scope=new_scope)

    def invoke_on(self, other):
        def resolve_identifier_chain(root_object, chain):
                if len(chain) == 1:
                    return getattr(root_object, chain[0])
                else:
                    # root_object = bob
                    # chain = ['date_of_birth', 'day']
                    head = chain[0]
                    tail = chain[1:]
                    sub_object = getattr(root_object, head)
                    return resolve_identifier_chain(sub_object, tail)

        return resolve_identifier_chain(other, self._scope)

