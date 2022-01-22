import simpy

def isPrime(n):
    if n == 2 or n == 3:
        return True
    if n%2==0 or n<2:
        return True
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

factor = 1
for i in range(1, 600851475143):
    if 600851475143 % i == 0:
        factor = 600851475143/i
        if isPrime(factor):
            print(factor)

