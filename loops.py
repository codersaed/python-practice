# Print numbers from 1 to 5
for i in range(1, 6):
    print(i)

# Sum of numbers from 1 to 10
total = 0
for i in range(1, 11):
    total += i
print("Total Sum:", total)

# Print each letter of a word
word = "Python"
for letter in word:
    print(letter)

# While loop example
count = 1
while count <= 5:
    print("Count:", count)
    count += 1

# Loop with condition
numbers = [10, 15, 20, 25, 30]
for num in numbers:
    if num % 2 == 0:
        print(num, "is even")
    else:
        print(num, "is odd")