# Get the absolute path of hello.txt
import os

if os.path.exists("hello.txt"):
    print("file exists")
else:
    print("file does not exist")

