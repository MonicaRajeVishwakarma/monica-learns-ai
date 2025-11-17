# Day 5 Notes – Functions

## Basic Function
```python
def greet():
    print("Hello Monica!")

greet()
```

## Function With Parameter
```python
def greet_baby(name):
    print("Hello", name)

greet_baby("Leo")
```

## Function With Return
```python
def add_numbers(a, b):
    return a + b

result = add_numbers(3, 5)
print(result)
```

## Default Parameter
```python
def welcome(name="Leo"):
    print("Welcome,", name)

welcome()
welcome("Monica")
```