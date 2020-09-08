# Program to illustrate the use of __init__() method

class ABC:
    def __init__(self,val):
        print("In class method ..")
        self.val = val
        print("the value is :", val)

obj = ABC(10)
