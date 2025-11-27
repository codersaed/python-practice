def get_number(text):
    while True:
        try:
            return float(input(text))
        except:
            print("Please enter a valid number!")

class Calculator:

    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        if b == 0:
            return "Error: Cannot divide by zero"
        return a / b

    def menu(self):
        print("\n--- Calculator Menu ---")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

    def run(self):
        while True:
            self.menu()
            choice = input("Choose option: ")

            if choice == "5":
                print("Thanks for using calculator!")
                break

            num1 = get_number("Enter first number: ")
            num2 = get_number("Enter second number: ")

            if choice == "1":
                print("Result:", self.add(num1, num2))
            elif choice == "2":
                print("Result:", self.subtract(num1, num2))
            elif choice == "3":
                print("Result:", self.multiply(num1, num2))
            elif choice == "4":
                print("Result:", self.divide(num1, num2))
            else:
                print("Invalid option!")

calc = Calculator()
calc.run()
