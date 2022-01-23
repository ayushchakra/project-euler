counter = 1
largestCount = 1
largestNum = 1
for i in range(1, 1000000):
    currentNum = i
    print(i)
    while currentNum > 1:
        counter += 1
        if currentNum%2 == 0:
            currentNum = currentNum / 2
        else:
            currentNum = 3*currentNum + 1
    if(counter>largestCount):
        largestCount = counter
        largestNum = i
    counter = 1
print(largestNum)