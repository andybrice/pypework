from pypework import FunctionCatcher
from functions import *

## Unit Tests ##

def test_function_catcher_exists():
    assert FunctionCatcher

def test_function_catcher_instantiates_with_no_arguments():
    f = FunctionCatcher()
    assert f.__class__ == FunctionCatcher

def test_function_catcher_instantiates_with_named_scope():
    f = FunctionCatcher( scope = __name__ )
    assert f.__class__ == FunctionCatcher

def test_function_catcher_scope_named():
    current_module = __import__(__name__)
    f = FunctionCatcher( scope = __name__ )
    assert f._identifier_chain == current_module

def test_function_catcher_scope_automatic():
    current_module = __import__(__name__)
    f = FunctionCatcher()
    assert f._identifier_chain == current_module
