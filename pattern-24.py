for i in range(5):
    for j in range(i+1):
        print("*",end='')
    for j in range(10-2*(i+1)):
        print(" ",end='')
    for j in range(i+1):
        print("*",end='')
    print()

for i in range(4,0,-1):
    for j in range(i):
        print("*",end='')
    for j in range(10-2*i):
        print(" ",end='')
    for j in range(i):
        print("*",end='')
    print()