num = int(input("Enter a positive number: "))
if num < 0:
    raise ValueError("Negative number not allowed!")
else:
    print("You entered:", num)

# custom 
class TooShortError(Exception):
    pass

text = input("Enter text: ")
if len(text) < 5:
    raise TooShortError("Text is too short!")
else:
    print("Text accepted!")