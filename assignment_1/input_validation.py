# Input Validation

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")

num = get_number("Enter a number: ")
print("You entered:", num)