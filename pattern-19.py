'''
A
BB
CCC
DDDD
EEEEE
'''
for i in range(5):
    for j in range(i+1):
        print(chr(65+i),end='')
    print()