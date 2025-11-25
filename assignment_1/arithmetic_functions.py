# Arithmetic functions

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

print(add(10, 5))
print(subtract(20, 7))
print(multiply(3, 9))
print(divide(10, 0))