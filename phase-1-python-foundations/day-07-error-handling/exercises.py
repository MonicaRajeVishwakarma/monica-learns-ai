# Day 07 -  Error Handling

# 1. Handling a ZeroDivisionError
print("Exercise 1:")
try:
    result = 10/0
except ZeroDivisionError:
    print("Cannot divide by zero")

# 2. Handling multiple exceptions
print("\nExercise 2:")
try:
    num = int((input("Enter a number:")))
    print( 10 / num)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid input! Please enter a valid number.")

# 3. Using else with try-except
print("\nExercise 3:")
try:
    x = 5
    y = 2
    result = x / y
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print("Division successful:",result)

# 4. Using finally
print("\nExercise 4:")
file = None
try:
    file = open("sample.txt", "w")
    file.write("Hello, AI world!")
finally:
    if file is not None:
        file.close()
        print("File closed successfully.")

# 5. Raising your own exception
print("\nExercise 5:")
def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return f"Age is {age}"

try:
    print(check_age(-1))
except ValueError as e:
    print("Error",e)