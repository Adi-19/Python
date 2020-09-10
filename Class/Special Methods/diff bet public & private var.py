# Program to illustrate the difference between public and private variables

class ABC():
    def __init__(self,var1,var2):
        self.var1 = var1
        self.__var2 = var2

    def display(self):
        print("From class method , Var1=",self.var1)
        print("From class method , Var2=",self.__var2)

obj = ABC(10,20)
obj.display()
print("From main module,Var1=",obj.var1)
print("From main module,Var2=",obj.__var2)  # It will throw error since it is private

#print("From main module,Var2=",obj._ABC__var2) To remove the error

