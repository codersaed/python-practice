# Basic decorator
def my_decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

# Decorator with arguments
def decorator_with_args(func):
    def wrapper(name):
        print(f"--- Start ---")
        func(name)
        print(f"--- End ---")
    return wrapper

@decorator_with_args
def greet(name):
    print(f"Hi {name}, welcome!")

greet("Saed")