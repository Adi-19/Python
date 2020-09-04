# Program to calculate GCD using recursive function

def GCD(x,y):
    rem = x%y
    if(rem==0):
        return y
    else:
        return GCD(y,rem)

n = int(input("Enter First number:"))
m = int(input("Enter Second number:"))
print("GCD of number is" , GCD(n,m))
