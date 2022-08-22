n = int(input('Enter the no. of rows: '))

for i in range(0,n):
    for k in range(0,i+1):
        print(' *',end='')
    print()
for i in range(n,0,-1):
    for j in range(i-1,0,-1):
        print(' *',end='')
    print()