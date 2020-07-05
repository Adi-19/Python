#WAP to find factorial of number using While loop

# number to find the factorial of
number = int(input("enter number"))
product = 1
current = 1

while  current <= number:
    # multiply the product so far by the current number
    product *= current
    # increment current with each iteration until it reaches number
    current += 1


# print the factorial of number
print(product)
