import random
import secrets

def GCD(a,b):
    while a*b !=0:
        if (a > b):
            a = a % b
        else:
            b = b % a
    return a+b


random_number1 = int(secrets.randbits(64))
random_number2 = int(secrets.randbits(64))
print(random_number1)
print(random_number2)

gcd_rd1_rd2 = GCD(random_number1, random_number2)
print(f"GCD({random_number1,random_number2}): {gcd_rd1_rd2}")

