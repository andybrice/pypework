# Pypework Roadmap #

### Smart Argument Order Handling

```python
100 >> subtract(10) # -> 90
100 >> subtract(10, ____) # -> -90
```

### Pipeable Methods and Properties

### Input Properties in Calls

### Deferred Execution

Chain together a sequence of pipeable functions with no input. To create a pipeline object which can be called or piped into later.

```python
sanitize = f.lowercase >> f.replace(" ", "_")

"Lorem Ipsum" >> sanitize # -> "lorem_ipsum"

sanitize("Lorem Ipsum") # -> "lorem_ipsum"
```

### Unified Function Catcher

Merge the _Function Catcher_ and the _Partial Function Catcher_ into one class with no significant detriment to performance.

## Ultimate Goals ##

Completely recreate the F# pipeline syntax in Python without the need for added cruft.

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
