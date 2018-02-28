# Pypework #

Pypework is a functional pipeline library for Python.

It allows you to rewrite messy function compositions such as this:

```python
title_sanitized =
    replace(replace(replace(lowercase("Lorem Ipsum Dolor 2018/02/18"), " ", "_"), "/", "-"), "@", "at")
```

In a far more readable format like this:

```python
title_sanitized = (
	"Lorem Ipsum Dolor 2018/02/18"
	>> f.lowercase
	>> f.replace("/", "-")
	>> f.replace(" ", "_")
	>> f.replace("@", "at")
)

title_sanitized # -> "lorem_ipsum_dolor_2018-02-18"
```

## Installation ##

Install using PIP by running:

```console
pip install pypework
```

## Usage ##

Import using:

```python
import pypework
```

Initialize using:

```python
default_namespace = __import__(__name__)
f = pypework.FunctionCatcher(default_namespace)
```

You can now make any function pipeable by adding `f.` before it. For example `lowercase()` becomes `f.lowercase`.
Trailing parentheses are optional if the function has only one argument.

Use the `>>` operator to pipe into the function like so:

```python
"Lorem Ipsum" >> f.lowercase # -> "lorem ipsum"
```

Or chain together multiple functions:

```python
"Lorem Ipsum" >> f.lowercase >> f.replace(" ", "_") # -> "lorem_ipsum"
```

You can also split a pipeline across multiple lines if you wrap it in parentheses:
```python
( "Lorem Ipsum"
  >> f.lowercase
  >> f.replace(" ", "_")
)
```
