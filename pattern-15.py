'''
1      1
12    21
123  321
12344321
'''
for i in range(4):
    # Numbers
    for j in range(i+1):
        print(j+1,end='')
    # Space
    for j in range(8-2*(i+1)):
        print(" ",end='')
    # Numbers
    for j in range(i,-1,-1):
        print(j+1,end='')

    print()