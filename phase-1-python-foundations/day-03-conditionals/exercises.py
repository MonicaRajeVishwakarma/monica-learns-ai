# Day 3 - Conditionals (if, elif, else)

# 1. Simple if
age = 14
if age > 12:
    print("Leo is growing fast")

# 2. If-else
milk = 0.1
if milk > 0.2:
    print("Enough milk left")
else:
    print("Need to restock milk")

# 3. If-elif-else
weather = "rainy"
if weather == "sunny":
    print("Go for a walk")

elif weather == "rainy":
    print("Stay inside and relax")
else:
    print("Check the weather again")

# 4. Logical Operators
age = 14
# if 10 < age < 20 (Simplified chain comparison)
if age > 10 and age < 20:
    print("Leo is between 10 and 20 weeks old")

# 5. Mini challenge
leo_sleep_hours = 14

if leo_sleep_hours > 15:
    print("Leo slept really well today")
elif leo_sleep_hours >= 12:
    print("A normal day of sleep")
else:
    print("Maybe a bit fussy today")
