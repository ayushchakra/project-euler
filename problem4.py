straight = 0
reversed = 0
largestPalindrome = 0

for i in range(500, 1000):
    for j in range(500, 1000):
        straight = i*j
        temp = i*j
        for k in range(5, -1, -1):
            reversed += (straight%10)*10**k
            straight = int(straight/10)
        if(reversed == temp):
            if(i*j>largestPalindrome):
                largestPalindrome = i*j
        reversed = 0

print(largestPalindrome)