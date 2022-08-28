#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = 10 - (number % 10)
ans = f"The last digit of {number} is {last_digit}"
if last_digit > 5:
    ans += "and is greater than 5"
elif last_digit == 0:
    ans += "and is 0"
else:
    ans += "and is less than 6 and not 0"
print(ans)
