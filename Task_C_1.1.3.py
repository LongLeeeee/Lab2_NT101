import random

def isprime(prime):
    if prime < 1 : return False
    if prime <= 3: return True
    if prime % 2 == 0 : return False
    if prime % 3 == 0: return False

    r= 0
    d = prime - 1
    while d % 2 == 0:
        r+=1
        d//=2
    for _ in range(5):
        a = random.randint(2, prime - 2)
        x = pow(a, d, prime)
        if x == 1 or x == prime - 1 :
            continue
        for _ in range(r - 1):
            x =  pow(x,2,prime)
            if prime == x-1:
                break
        else:
            return False
    return True 

number1 = pow(2,89) - 1
number2 = random.randint(2, number1)
if isprime(number2):
    print(f"{number2} is a prime number")
else:
    print(f"{number2} isn't a prime number")

