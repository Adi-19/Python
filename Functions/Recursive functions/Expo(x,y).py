def exp(x,y):
    if(y==0):
        return 1
    else:
        return (x*exp(x,y-1))

n = int(input("Enter First number:"))
m = int(input("Enter Second number:"))
print("Result" , exp(n,m))
