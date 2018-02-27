# Pypework

## Pypework is a functional pipeline library for Python.

It allows you to rewrite messy function compositions such as this:

```python
title_sanitized = replace(replace(replace(lowercase("Lorem Ipsum Dolor 2018/02/18"), " ", "_"), "/", "-"), "@", "at")
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