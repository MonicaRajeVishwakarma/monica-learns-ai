# Day 6 Notes – Modules and Imports

## Importing Built-in Modules
```python
import math
print(math.sqrt(16))
print(math.pi)
```

## Importing Specific Functions
```python
from math import sqrt
print(sqrt(25))
```

## Importing with an Alias
```python
import math as m
print(m.cos(0))
```

## Creating a Custom Module
# my_utils.py
```python
def greet(name):
    return f"Hello, {name}"
```

## Importing Your Own Module
```python
import my_utils
print(my_utils.greet("Monica"))
```