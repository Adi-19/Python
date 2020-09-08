# Program to access class members using the class object

class ABC:
    var = 10
    def display(self):
        print("In class method")

obj = ABC()
print(obj.var)
obj.display()
