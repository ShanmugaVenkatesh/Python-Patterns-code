for i in range(5):
    # Space
    for j in range(4-i):
        print(' ',end='')
    # Star
    for j in range(2*i+1):
        print('*',end='')
    # Space
    for j in range(4-i):
        print(' ',end='')
    print()