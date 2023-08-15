'''
    A
   ABC
  ABCDE
 ABCDEFG
ABCDEFGHI
'''
for i in range(5):
    for j in range(4-i):
        print(' ',end='')
    for j in range(2*i+1):
        print(chr(65+j),end='')
    '''for j in range(4-i):
        print(' ',end='')'''
    print()