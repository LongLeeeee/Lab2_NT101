import secrets 
import math
import random
def isprime(prime):
    if prime <= 1: return False
    if prime <= 3: return True
    if prime % 2 == 0: return False
    if prime % 3 == 0: return False
    r = 0 
    d = prime - 1
    while d % 2 == 0:
        r += 1
        d //= 2
    for _ in range(5):
        a = random.randint(2, prime - 2) 
        x = pow(a, d, prime) 
        if x == 1 or x == prime - 1: continue
        for _ in range(r - 1):
            x = pow(x, 2, prime) 
            if x == prime - 1: break
        else: return False
    return True   
def generate_random_prime(bit_length):
    while True:
        random_number = int(secrets.randbits(bit_length))
        if isprime(random_number) and random_number > 1:
            return random_number
while True:
    try:
        option = int(input("Enter the number of bits you want (1: 8-bits, 2: 16-bits, 3: 64-bits): "))
        if option == 1:
            prime_number = generate_random_prime(8)
            print (f"A random prime number: {prime_number}")
        elif option == 2:
            prime_number = generate_random_prime(16)
            print (f"A random prime number: {prime_number}")
        elif option == 3:
            prime_number = generate_random_prime(64)
            print (f"A random prime number: {prime_number}")
    except ValueError:
            print("Please enter a valid integer.")

