from pypework import PartialCatcher, PartialPipeFunction, ____
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

def test_pipes_single_argument_with_parentheses(p):
    x = 5 >> p.increment()
    assert x == 6

def test_pipes_single_argument_without_parentheses(p):
    x = 5 >> p.increment
    assert x == 6

def test_pipes_multiple_arguments(p):
    x = 5 >> p.add(5)
    assert x == 10

def test_chains(p):
    x = 5 >> p.double >> p.increment >> p.add(4)
    assert x == 15

## Placeholder Piping ##

def test_pipes_placeholder_in_first_argument(p):
    x = 10 >> p.subtract(____, 5)
    assert x == 5

def test_pipes_placeholder_in_subsequent_argument(p):
    x = 5 >> p.subtract(10, ____)
    assert x == 5

def test_pipes_placeholder_in_multiple_arguments(p):
    x = 5 >> p.add(____, ____)
    assert x == 10   

def test_pipes_placeholder_in_multiple_arguments(p):
    x = 5 >> p.add(____, ____)
    assert x == 10   

def test_pipes_placeholder_in_keywords(p):
    x = 2 >> p.distance(7, 10, multiplier=____)
    assert x == 6