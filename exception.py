#try and except are a way f handling errors in python
#try block is used to test a block of code for errors
#except block is used to handle the errors
try:
    with open("none.txt") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found. Please check the file path and try again.")