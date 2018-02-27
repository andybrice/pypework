## Functions ##

class PipelineStage:
    def __init__(self, function, *arguments, **keywords):
        self.function = function
        self.arguments = arguments
        self.keywords = keywords

    def __call__(self, operand):
        return self.function(operand, *self.arguments, **self.keywords)

f = PipelineStage

def pipe(operand, *operations):
    if operations:
        head = operations[-1]
        tail = operations[:-1]

        return head( pipe(operand, *tail) )

    else: return operand

## Example ##

from example_functions import *

# pipe( 5,
#     f (increment),
#     f (double),
#     f (add, 3)
#     )
