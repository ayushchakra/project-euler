cont = True
counter = 2*3*5*7*11*13*17*19
while cont:
    print(counter)
    for i in range(1, 21):
        if counter % i != 0:
            counter += 2*3*5*7*11*13*17*19
            break
        if i == 20:
            cont = False
            print(counter)