'''
E
DE
CDE
BCDE
ABCDE
'''
for i in range(5):
    for j in range(i,-1,-1):
        print(chr(65+4-j),end='')
    print()