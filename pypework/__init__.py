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
        placeholder_in_arguments = ____ in self.arguments
        placeholder_in_keywords  = ____ in self.keywords.values()
        placeholder_in_call = placeholder_in_arguments or placeholder_in_keywords

        if placeholder_in_arguments:
            arguments = [operand if a==____ else a for a in self.arguments]
        else:
            arguments = self.arguments

        if placeholder_in_keywords:   
            keywords = { k:operand if v==____ else v for (k,v) in self.keywords.items() }
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
