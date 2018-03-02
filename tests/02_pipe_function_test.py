from pypework import PipeFunction
from functions import *

### Pipe Function ###

def test_exists():
    assert PipeFunction

def test_instantiates_with_function_with_single_argument():
    f = PipeFunction(increment)
    assert f
    assert f.function == increment

def test_calls_function_with_single_argument():
    f = PipeFunction(increment)
    assert f(5) == 6

def test_instantiates_with_function_with_multiple_arguments():
    f = PipeFunction(add, 5)
    assert f.function == add

def test_calls_function_with_multiple_arguments():
    f = PipeFunction(add, 5)
    assert f(10) == 15

def test_pipes_with_single_argument():
    f = PipeFunction(increment)
    assert (4 >> f) == 5

def test_pipes_with_multiple_arguments():
    f = PipeFunction(add, 5)
    assert (5 >> f) == 10

def test_chains():
    f = PipeFunction(increment)
    g = PipeFunction(double)
    assert (4 >> f >> g) == 10
