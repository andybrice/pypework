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
        arguments = [operand if a==____ else a for a in self.arguments]
        keywords  = { k:operand if v==____ else v for (k,v) in self.keywords.items() }
        return self.function(*arguments, **keywords)

## Identifier Chain Processor Classes ##

class AbstractIdentifierCatcher:
    def __init__(self, _identifier_chain=None, namespace=None):
        self._identifier_chain = _identifier_chain or __import__(namespace)

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
