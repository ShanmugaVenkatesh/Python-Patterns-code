for i in range(5,0,-1):
    # Space
    for j in range(5-i):
        print(' ',end='')
    # Star
    for j in range(2*i-1):
        print('*',end='')
    # Space
    for j in range(5-i):
        print(' ',end='')
    print()