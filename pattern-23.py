# 1st half 
for i in range(5,0,-1):
    # Star
    for j in range(i):
        print("*",end='')
    # Space
    for j in range(10-2*i):
        print(" ",end='')
    # Star
    for j in range(i):
        print("*",end='')
    print()

# 2nd Half    
for i in range(5):
    for j in range(i+1):
        print("*",end='')
    for j in range(10-2*(i+1)):
        print(" ",end='')
    for j in range(i+1):
        print("*",end='')
    print()