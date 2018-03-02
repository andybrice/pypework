from pypework import PartialCatcher
from functions import *

## Unit Tests ##

def test_function_catcher_exists():
    assert PartialCatcher

def test_function_catcher_instantiates_with_no_arguments():
    f = PartialCatcher()
    assert f.__class__ == PartialCatcher

def test_function_catcher_instantiates_with_named_scope():
    f = PartialCatcher( scope = __name__ )
    assert f.__class__ == PartialCatcher

def test_function_catcher_scope_named():
    current_module = __import__(__name__)
    f = PartialCatcher( scope = __name__ )
    assert f._identifier_chain == current_module

def test_function_catcher_scope_automatic():
    current_module = __import__(__name__)
    f = PartialCatcher()
    assert f._identifier_chain == current_module
