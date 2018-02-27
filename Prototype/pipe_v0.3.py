## Functions ##

class PipeFunction:
    def __init__(self, function, *arguments, **keywords):
        self.function = function
        self.arguments = arguments
        self.keywords = keywords

    def __call__(self, operand):
        return self.function(operand, *self.arguments, **self.keywords)

    def __rrshift__(self, other):
        return self(other)

f = PipeFunction

## Example ##

from example_functions import *

(5
    >> f(increment)
    >> f(lambda x: x * 2)
    >> f(add, 3)
)
