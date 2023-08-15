'''
   A
  ABA
 ABCBA
ABCDCBA
'''

'''
for i in range(5):
    # Space
    for j in range(4-i):
        print(' ',end='')
    # Alphabhet
    for j in range(i+1):
        print(chr(65+j),end='')
    # Reversing Alphabet
    for j in reversed(range(i)):
        print(chr(65+j),end='')
    # Space
    for j in range(4-i):
        print(' ',end='')
    print()
'''

for i in range(5):

    # Space
    for j in range(4-i):
        print(' ',end='')

    # Alphabet
    for j in range(i+1):
        print(chr(65+j),end='')

    # Reversing Alphabhet
    for j in range(i - 1, -1, -1):
        print(chr(65 + j), end='')

    print()