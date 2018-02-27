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
    def __init__(self, identifier_chain):
        self.identifier_chain = identifier_chain

    def __getattr__(self, name):
        return self.__class__( getattr(self.identifier_chain, name) )

    def __rrshift__(self, other):
        return self()(other)

class FunctionCatcher(AbstractIdentifierCatcher):
    def __call__(self, *arguments, **keywords):
        return PipeFunction(self.identifier_chain, *arguments, **keywords)

class PartialFunctionCatcher(AbstractIdentifierCatcher):
    def __call__(self, *arguments, **keywords):
        return PartialPipeFunction(self.identifier_chain, *arguments, **keywords)

## Placeholders ##

class InputPlaceholder: pass

## Interface ##

____ = InputPlaceholder()
