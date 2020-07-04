# WAP to guess a number

answer = 35
guess = 45   # this is just a sample answer and guess

if guess < answer:
    result = "Oops!  Your guess was too low."
elif guess > answer:
   result = "Oops!  Your guess was too high."
elif guess==answer:
    result = "Nice!  Your guess matched the answer!"
print(result)
