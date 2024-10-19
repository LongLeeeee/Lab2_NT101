import math
import random

n = 100
prime_matrix = [True]*n 
def eratosthenes(primes):
    for i in range(2, n):
        if prime_matrix[i] == True:
            primes.append(i)
            for j in range(i*2, n, i):
                prime_matrix[j] = False

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

def find_mersenne_primes(matrix, count):
    for i in matrix:
       mersenne_prime = 2**i - 1
       if isprime(mersenne_prime) == True:
           count+=1 
           print(f"{mersenne_prime}")
           if count == 10:
               break

count = 10
primes = []
eratosthenes(primes)
print("10 số nguyên tố Mersenne đầu tiên:")
find_mersenne_primes(primes, count)

