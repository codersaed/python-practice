# Writing to hello.txt 
with open("hello.txt", "w") as file:
    file.write("hello, python")

# Reading the file
with open("hello.txt", "r") as file:
    content = file.read()
    print(content)

# Appending to hello.txt
with open("hello.txt", "a") as file:
    file.write("\nWelcome to File Handling!")

# Reading updated file
with open("hello.txt", "r") as file:
    content = file.read()
    print(content)