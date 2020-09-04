def fact(n):
    if(n==1 or n==0):
        return n
    else:
        return n*fact(n-1)

n = int(input("Enter value of n:"))
print("factorial of number" ,n, "is", fact(n))
