from pypework import PartialCatcher, PartialPipeFunction
from functions import *
import pytest

@pytest.fixture
def p(): return PartialCatcher( scope = __name__ )

## Function Catching ##

def test_instantiates_without_parentheses(p):
    x = p.increment
    assert x
    assert x.__class__ == PartialCatcher

def test_instantiates_with_parentheses(p):
    x = p.increment()
    assert x
    assert x.__class__ == PartialPipeFunction

def test_catches_function_without_parentheses(p):
    x = p.increment
    assert x._identifier_chain == increment

def test_catches_function_with_parentheses(p):
    x = p.increment()
    assert x.function == increment

## Function Piping ##

# def test_pipes_single_argument_with_parentheses(p):
#     x = 5 >> p.increment()
#     assert x == 6
#
# def test_pipes_single_argument_without_parentheses(f):
#     x = 5 >> f.increment
#     assert x == 6
#
# def test_pipes_multiple_arguments(f):
#     x = 5 >> f.add(5)
#     assert x == 10
#
# def test_inline_pipeline(f):
#     x = 5 >> f.double >> f.increment >> f.add(4)
#     assert x == 15
