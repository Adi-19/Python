# Program to differentiate between class and object variables

class ABC:
    class_var = 0
    def __init__(self,var):
        ABC.class_var+= 1
        self.var = var
        print("The object value is :", var)
        print("The Value of class variable is :",ABC.class_var)

obj = ABC(20)
obj = ABC(30)
obj = ABC(40)
