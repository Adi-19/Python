# Program to demonstrate flow of control after the return statement.
def display():
    print("In function")
    print("About to extecute return statement")
    return()
print("This line will never be displayed")
display()
print("Back to the caller")
