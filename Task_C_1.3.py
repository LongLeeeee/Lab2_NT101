
def pow1(a, x, p):
    result = 1
    a = a % p

    while x > 0:
        if x % 2 == 1: 
            result = (result*a) % p
        x//=2
        a = (a*a) % p
    return result

number1 = int(input("Enter the base (a): "))
number2 = int(input("Enter the exponent (x): "))
number3 = int(input("Enter the modulus (p): "))

number =  pow1(number1,number2,number3)
print(f"Result: {number}")