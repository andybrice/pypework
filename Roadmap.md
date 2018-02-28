# Pypework Roadmap #

### Simple Initialization

Import and initialize without needing to manually instantiate catchers or specify the default namespace.

```python
from pypework import f, p, m, ____
```

### Pipeable Methods and Properties

Chain together functions and methods or properties in any order.

```python
[1,2,3,2,3,3,1,2,3,2] >> f.filter(3).length >> f.increment # -> 5
```
or

```python
[1,2,3,2,3,3,1,2,3,2] >> f.filter(3) >> m.length >> f.increment # -> 5
```

### Input Properties in Calls

Reference properties of the input object as values in function arguments.

```python
square_array = [1,2,3] >> f.tile_array(____.length)

square_array # -> [[1,2,3],
             #     [1,2,3],
             #     [1,2,3]]
```

### Deferred Execution

Chain together a sequence of pipeable functions with no input. To create a pipeline object which can be called or piped into later.

```python
sanitize = f.lowercase >> f.replace(" ", "_")

"Lorem Ipsum" >> sanitize # -> "lorem_ipsum"
sanitize("Lorem Ipsum") # -> "lorem_ipsum"
```
### Smart Argument Order Handling

Enable the _Partial Function Catcher_ automatically detect when input is to the first argument. 

```python
100 >> p.subtract(10) # -> 90
10 >> p.subtract(100, ____) # -> 90
```

### Unified Function Catcher

Merge the _Function Catcher_ `f` and the _Partial Function Catcher_ `p` into one class with no significant detriment to performance.

## Ultimate Goals ##

Recreate the F# pipeline syntax in Python without the need for added visual cruft.

```python
"Lorem Ipsum" |> lowercase |> replace(" ", "_") # -> "lorem_ipsum"

```

```python
"Lorem Ipsum"
  |> lowercase
  |> replace(" ", "_")

 # -> "lorem_ipsum"
```

(Until Python hopefully implements it natively, as is currently planned for JavaScript.)
