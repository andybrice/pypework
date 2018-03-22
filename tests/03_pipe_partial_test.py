from pypework import PartialPipeFunction
from functions import *

### Pipe Function ###

def test_exists():
    assert PartialPipeFunction

def test_instantiates_with_function_with_single_argument():
    p = PartialPipeFunction(increment)
    assert p
    assert p.function == increment

# def test_calls_function_with_single_argument():
#     p = PartialPipeFunction(increment)
#     assert p(5) == 6

def test_instantiates_with_function_with_multiple_arguments():
    p = PartialPipeFunction(add, 5)
    assert p.function == add

# def test_calls_function_with_multiple_arguments():
#     p = PartialPipeFunction(add, 5)
#     assert p(10) == 15

# def test_pipes_with_single_argument():
#     p = PartialPipeFunction(increment)
#     assert (4 >> p) == 5

# def test_pipes_with_multiple_arguments():
#     f = PartialPipeFunction(add, 5)
#     assert (5 >> f) == 10

# def test_chains():
#     f = PartialPipeFunction(increment)
#     g = PartialPipeFunction(double)
#     assert (4 >> f >> g) == 10
