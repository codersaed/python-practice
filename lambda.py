# Simple lambda example
square = lambda x: x * x
print("Square of 10:", square(10))

# Lambda with multiple parameters
add = lambda a, b: a + b
print("Sum:", add(3, 4))

# Lambda with conditional expression
check_even = lambda x: "Even" if x % 2 == 0 else "Odd"
print(check_even(7))

# Using lambda with map()
nums = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x * x, nums))
print("Squares:", squares)

# Using lambda with filter()
evens = list(filter(lambda x: x % 2 == 0, nums))
print("Evens:", evens)

# Using lambda with sorted()
students = [("Saed", 25), ("Rakib", 20), ("Nusrat", 22)]
sorted_students = sorted(students, key=lambda x: x[1])
print("Sorted by age:", sorted_students)