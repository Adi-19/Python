# Program to demonstrate modifying a global variable
var = "Good"
def show():
    global var
    var = "Morning"
    print("In Function var is", var)
show()

print("Outside function var is", var)

var = "Fantastic"
print("Outside function, after modification, var is ",var)
