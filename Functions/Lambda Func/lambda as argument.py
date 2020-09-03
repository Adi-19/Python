# Program to pass lambda func as an argument to function
def func(f,n):
    print(f(n))
square = lambda x:x**2
cube= lambda x:x**3

func(square,4)
func(cube,3)

