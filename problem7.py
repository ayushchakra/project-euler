counter = 1
i = 0
def isPrime(n):
    if n == 2 or n == 3:
        return True
    if n%2==0 or n<2:
        return False
    for i in range(2,int(n/2)):
        if n%i==0:
            return False
    return True

while counter <= 10001:
    i += 1
    if isPrime(i):
        counter += 1
        print(counter)
print(i)