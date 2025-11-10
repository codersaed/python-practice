# Check if a number is even or odd
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# Take two numbers and show their sum
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Sum:", a + b)

# Check if a person is adult or child
age = int(input("Enter your age: "))
if age >= 18:
    print("You are an Adult")
else:
    print("You are a Child")

# Check positive or negative
n = int(input("Enter a number: "))
if n > 0:
    print("Positive")
elif n < 0:
    print("Negative")
else:
    print("Zero")

# Find the largest among three numbers
a = int(input("Enter first: "))
b = int(input("Enter second: "))
c = int(input("Enter third: "))

if a > b and a > c:
    print("Largest:", a)
elif b > a and b > c:
    print("Largest:", b)
else:
    print("Largest:", c)

# Count number of letters in a name
name = input("Enter your name: ")
print("Your name has", len(name), "letters")