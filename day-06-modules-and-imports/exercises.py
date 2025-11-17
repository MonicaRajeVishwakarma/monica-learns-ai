# Day 06 - Modules and Imports

# 1. Importing a built-in module
import math
from math import factorial
print("square root of 36:",math.sqrt(36))
print("value of pi",math.pi)

# 2. Importing specific functions
print("Factorial of 5 using specific function",factorial(5))
print("Factorial of 5 using main module",math.factorial(5))

#3. Using alias
import math as m
print("Cosine of 0 :", m.cos(0))

#4. Importing your own module
import my_utils
print(my_utils.greet("Monica"))



