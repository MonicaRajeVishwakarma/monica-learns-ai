# Day 7 Notes – Error Handling

## What Are Exceptions?
An **exception** is an error that occurs during program execution.  
Instead of crashing, Python allows us to handle these errors gracefully using `try` and `except`.

Common exceptions:
- `ZeroDivisionError`
- `ValueError`
- `TypeError`
- `FileNotFoundError`

---

## Basic Try-Except
Use `try` to run code and `except` to catch errors.

```python
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
