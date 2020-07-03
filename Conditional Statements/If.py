# WAP to show the use of If statment
phone_balance = int(input("enter the balence"))
bank_balance = 100

print(phone_balance, bank_balance)

if phone_balance < 5:
    phone_balance += 10
    bank_balance -= 10

print(phone_balance, bank_balance)

#the lines that increment phone_balance and decrement bank_balance only execute
#if it is true that phone_balance is less than 5. If not, the code in this if block is simply skipped.
# if the balence is less than 5 more balence 10 is added and subtracted from bank balance
