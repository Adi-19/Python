# Write a function to convert time into minutes

def conv_time_min(hrs,min):
    min = hrs*60 + min
    return min
h = int(input("enter hour"))
m = int(input("enter minutes"))
m = conv_time_min(h,m)
print("Minutes", m)
