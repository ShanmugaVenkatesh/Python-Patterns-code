'''
   1
  212
 32123
4321234
'''
for i in range(4):
    for j in range(4-i):
        print(" ",end='')
    for j in range(i,-1,-1):
        print(j+1,end='')
    for j in range(i):
        print(j+2,end='')
    print()