# WAP that lets the competitor know which of these prizes they won based on the number of points they scored
'''
Points	        Prize
1 - 50	        wooden rabbit
51 - 150	no prize
151 - 180	wafer-thin mint
181 - 200	penguin
'''

points = int(input("Enter your team points"))

if points <= 50:
    result = "Congratulations! You won a wooden rabbit!"
elif points <= 150:
    result = "Oh dear, no prize this time."
elif points <= 180:
    result = "Congratulations! You won a wafer-thin mint!"
else:
    result = "Congratulations! You won a penguin!"

print(result)
