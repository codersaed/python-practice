try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    result = a / b
    print("Result:", result)
except ZeroDivisionError:
    print("Cannot divide by zero!")


# Open a file safely and close it using finally
try:
    file = open("hello.txt", "r")
    print(file.read())
except FileNotFoundError:
    print("File not found!")
finally:
    print("Closing file...")
    file.close()