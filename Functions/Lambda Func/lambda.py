# Smaller of two number using lambda function
def small(a,b):
    if(a<b):
        return a
    else:
        return b
sum = lambda x,y :x+y
diff = lambda x,y : x-y
print("smaller of two numbers" ,small(sum(4,3),diff(3,2)))
