num1 = 10
print("Global variable num1=",num1)
def func(num2):
    print("In function num2 = " ,num2)
    num3 = 30
    print("In function num3 = " ,num3)
func(20)
print("num1 again=",num1)
print("num3 outside function =",num3) # it will throw error since is local variable.
