from pypework import FunctionCatcher, PipeFunction
from functions import *
import pytest

@pytest.fixture
def f(): return FunctionCatcher( scope = __name__ )

## Function Catching ##

def test_instantiates_without_parentheses(f):
    x = f.increment
    assert x
    assert x.__class__ == FunctionCatcher

def test_instantiates_with_parentheses(f):
    x = f.increment()
    assert x
    assert x.__class__ == PipeFunction

def test_catches_function_without_parentheses(f):
    x = f.increment
    assert x._identifier_chain == increment

def test_catches_function_with_parentheses(f):
    x = f.increment()
    assert x.function == increment

## Function Piping ##

def test_pipes_single_argument_with_parentheses(f):
    x = 5 >> f.increment()
    assert x == 6

def test_pipes_single_argument_without_parentheses(f):
    x = 5 >> f.increment
    assert x == 6

def test_pipes_multiple_arguments(f):
    x = 5 >> f.add(5)
    assert x == 10

def test_inline_pipeline(f):
    x = 5 >> f.double >> f.increment >> f.add(4)
    assert x == 15
