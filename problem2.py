import numpy as np

fibonacci = np.ones(1)
fibonacci = np.append(fibonacci, 2)

counter = 1
while fibonacci[counter]<4000000:
    fibonacci = np.append(fibonacci, fibonacci[counter] + fibonacci[counter-1])
    counter += 1
    if counter == 10:
        print(fibonacci)

sum = 0
for i in range(0, len(fibonacci)):
    if(fibonacci[i]%2==0):
        sum+=fibonacci[i]
print(sum)