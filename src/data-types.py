# Data types in Python
"""
numbers - interger, float
strings
boolean - True, False
"""

# 1. Operations
x = 10
y = 20.0
print(x + y)
print(f"power : {x**3}")
z = -10.50

print(10 / 2)  # 5.0 float value int/int
print(10 / 3)  # 3.333 float
print(10 // 3)  # 3 floor value, round-down

x += 2  # 12
x *= 2  # 24
x /= 2  # 12.0 float value

# always follows PEMDAS - peranthasis, exponential, mul, div, add, sub

# 2. String Operations
name = "Sachin"
print(len(name))
print(name.lower())
print(name.upper())
print(name.title())

sentence = "$ I am a cricketer "
print(len(sentence))
print(len(sentence.strip()))  # remove trailing spaces
print(len(sentence.strip("$")))

print(sentence.find("am"))  # 4 start posittion from 0
print("a" in sentence)


name = "sachin"
print(name.startswith("a"))
print(name.endswith("a"))
