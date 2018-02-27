## Classes ##

class PipeFunction:
    def __init__(self, function, *arguments, **keywords):
        self.function = function
        self.arguments = arguments
        self.keywords = keywords

    def __call__(self, operand):
        return self.function(operand, *self.arguments, **self.keywords)

    def __rrshift__(self, other):
        return self(other)

class IdentifierChainCatcher:
    def __init__(self, identifier_chain):
        self.identifier_chain = identifier_chain

    def __getattr__(self, name):
        return IdentifierChainCatcher( getattr(self.identifier_chain, name) )

    def __call__(self, *arguments, **keywords):
        return PipeFunction(self.identifier_chain, *arguments, **keywords)

    def __rrshift__(self, other):
        return self()(other)

default_namespace = __import__(__name__)

## Examples ##

import example_functions as xf

f = IdentifierChainCatcher(default_namespace)

5 >> f.add(1) >> f.increment
