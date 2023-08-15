'''
1
01
101
0101    
10101
'''
for i in range(5):
    if i%2==0:
        start=1
    else:
        start=0
    for j in range(i+1):
        print(start,end='')
        start=1-start
        '''if start==1: start=0
        else: start=1'''
    print()