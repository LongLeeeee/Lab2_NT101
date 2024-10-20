import random
import secrets 

def gcd(num1,num2):
    while num1*num2 !=0:
        if (num1 > num2):
            num1 = num1 % num2
        else:
            num2 = num2 % num1
    return num1+num2

def _pow(a, x, p):
    result = 1
    a = a % p
    while x > 0:
        if x % 2 == 1: 
            result = (result*a) % p
        x//=2
        a = (a*a) % p
    return result

def isprime(prime):
    if prime <= 1:
        return False
    if prime <= 3:
        return True
    if prime % 2 == 0:
        return False
    if prime % 3 == 0:
        return False
    r= 0
    d = prime - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    for _ in range(5):
        a = random.randint(2, prime - 2) 
        x = pow(a, d, prime) 
        if x == 1 or x == prime - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, prime) 
            if x == prime - 1:
                break
        else:
            return False
    return True 

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def mod_inverse(e, phi_n):
    gcd, x, _ = extended_gcd(e, phi_n)
    if gcd != 1:
        return -1
    else:
        return x % phi_n
    
def generate_random_prime():
    while True:
         number = int(secrets.randbits(64))
         if isprime(number): return number
while True:
    option = int(input("1. Encrypt\n2. Decrypt\nEnter your choice: "))
    if option == 1: 
        option = int(input("1. Enter number\n2. Generate random prime\nEnter your choice: "))
        if option == 1:
            p = int(input("Enter p: "))
            q = int(input("Enter q: "))
            e = int(input("Enter e: "))
            if isprime(q) == False: continue
            if isprime(p) == False: continue
            if isprime(e) == False: continue

            n = p*q
            phiN = (p-1)*(q-1)

            d = mod_inverse(e,phiN)
            if (d == -1): continue
            print(f"Public key (n,e): ({n},{e})")
            print(f"Private key (n,d): ({n},{d})")
            plaintext = input(f"Enter your plaintext: ")
            cyphertext = str()
            for i in plaintext:
                c = _pow(ord(i),e,n)
                cyphertext =cyphertext + str(c)

            print(f"Ciphertext: {cyphertext}")
        elif option == 2:
            p = 0
            q = 0
            while True:
                if isprime(p) == False: p = secrets.randbits(16)
                elif isprime(q) == False: q = secrets.randbits(16)
                else: break

            n = p*q
            phiN = (p-1)*(q-1)
            e = random.randint(2, phiN - 1)
            while True:
                if isprime(e) == False and gcd(e, phiN) != 1:
                    e = random.randint(2, phiN - 1)
                else: 
                    break
            d = mod_inverse(e,phiN)
            if (d == -1): continue

            print(f"P number: {p}")
            print(f"Q number: {q}")
            print(f"PhiN number: {phiN}")
            print(f"Public key (n,e): ({n},{e})")
            print(f"Private key (n,d): ({n},{d})")
            plaintext = input(f"Enter your plaintext: ")
            cyphertext = str()
            for i in plaintext:
                c = _pow(ord(i),e,n)
                c = hex(c)[2:]
                cyphertext = cyphertext + str(c) + " "

            print(f"Ciphertext: {cyphertext}") 
    elif option == 2:
        p = int(input("Enter p: "))
        q = int(input("Enter q: "))
        d = int(input("Enter d: "))
        temp_cyphertext = input(f"Enter your cyphertext: ")
        cyphertext = temp_cyphertext.split(' ')
        plaintext = str()
        for i in cyphertext:
            c = _pow(int(i,16),d,n)
            plaintext = plaintext + chr(int(c))
        print(f"Plaintext: {plaintext}")