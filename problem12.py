def isPrime(n):
    if n == 2 or n == 3:
        return True
    if n%2==0 or n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

def numOfFactors(n):
    primes = {}
    if n == 1:
        return 1
    while n%2 == 0:
        if 2 in primes:
            primes[2] = primes[2] + 1
        else: 
            primes[2] = 1
        n = n//2
    while n > 1:
        for i in range(2, n+1):
            if n%i == 0 and isPrime(i):
                if i in primes:
                    primes[i] = primes[i] + 1
                else: 
                    primes[i] = 1
                n = int(n / i)
                break
    counter = 1
    for key, value in primes.items():
        counter = counter * (value + 1)
    return counter

cont = True
i = 1
count = 2

while cont:
    if numOfFactors(i) > 500:
        cont = False
        print(i)
    i = i + count
    count += 1