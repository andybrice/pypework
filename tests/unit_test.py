import pypework

def test_module_imports():
    assert pypework

def test_function_catcher_exists():
    assert pypework.FunctionCatcher

def test_function_catcher_instantiates_with_no_arguments():
    f = pypework.FunctionCatcher()
    assert f.__class__ == pypework.FunctionCatcher

def test_function_catcher_instantiates_with_named_scope():
    f = pypework.FunctionCatcher( namespace = __name__ )
    assert f.__class__ == pypework.FunctionCatcher

def test_function_catcher_with_named_scope():
    current_module = __import__(__name__)
    f = pypework.FunctionCatcher( namespace = __name__ )
    assert f._identifier_chain == current_module

def test_function_catcher_with_automatic_scope():
    current_module = __import__(__name__)
    f = pypework.FunctionCatcher()
    assert f._identifier_chain == current_module

def increment(x): return x + 1
def add(a,b): return a + b

f = pypework.FunctionCatcher( namespace = __name__ )

def test_catches_function_with_parentheses():
    x = f.increment()
    assert x.__class__ == pypework.PipeFunction

def test_catches_function_without_parentheses():
    x = f.increment
    assert x.__class__ == pypework.FunctionCatcher

def test_pipes_single_argument_with_parentheses():
    x = 5 >> f.increment()
    assert x == 6

def test_pipes_single_argument_without_parentheses():
    x = 5 >> f.increment
    assert x == 6
