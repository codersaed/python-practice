# Simple function
def greet():
    print("Hello, welcome!")

greet()

# Function with parameters
def greet_user(name):
    print(f"Hello {name}, welcome!")

greet_user("Saed")

# Function returning value
def add(a, b):
    return a + b

result = add(10, 5)
print("Result:", result)

# Function with multiple parameters
def info(name, age, level):
    print(f"Name: {name}, Age: {age}, Level: {level}")

info("Demo", 20, "Beginner")

# Function with default parameters
def power(base, exp=2):
    return base ** exp

print("Square:", power(5))
print("Cube:", power(5, 3))