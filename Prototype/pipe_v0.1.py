## Functions ##

def pipe(operand, *operations):
    if operations:
        head = operations[-1]
        tail = operations[:-1]

        function  = head[0]
        arguments = head[1:]

        return function( pipe(operand, *tail), *arguments )

    else: return operand

## Example ##

# from example_functions import *

# pipe( 5
#     , [increment, {'by': 1}]
#     , [double]
#     , [add, 3]
#     , [double]
#     )
