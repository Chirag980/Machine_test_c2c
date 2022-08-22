

def show_numbers(limit):
    for i in range(1,limit):
        if i ==1:
            print(i,end='')
            print(' ODD')

        elif (i%2==0):
            print(i,end='')
            print(' EVEN')
        else:
            print(i,end='')
            print(' ODD')
print(show_numbers(4))