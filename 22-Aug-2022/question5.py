

class Calculator:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def add(self):
        return self.a + self.b
    def subtract(self):
        return self.a - self.b
    def multiplication(self):
        return self.a * self.b
    def division(self):
        return self.a / self.b
    def exit(self):
        return ('Exiting!')

a = int(input('Enter first number: '))

b = int(input('Enter second number: '))
obj = Calculator(a,b)

while True:
    def menu():
        x = ('0.Exit\n1.Add\n2.Subtraction\n3.Multiplication\n4.Division')
        print(x)
    menu()
    choice= int(input('Enter Choice: '))

    if choice ==1:
        print('Result: ',obj.add())
    elif choice ==2:
        print('Result: ',obj.subtract())
    elif choice ==3:
        print('Result: ',obj.multiplication())
    elif choice ==4:
        print('Result: ',obj.division())
    elif choice ==0:
        print(obj.exit())
        break
    else:
        print('Inalid Option')
        break
