class Calculator :	
    def __init__(self, num1, num2) :
        self.num1 = num1
        self.num2 = num2
    
    def add(self) :
        return self.num1 + self.num2

    def sub(self) :
        return self.num1 - self.num2

    def mul(self) :
        return self.num1 * self.num2

    def sub(self) :
        return self.num1 / self.num2

a = 10
b = 20

cal1 = Calculator(a, b)

print('%d + %d = %d' % (a, b, cal1.add()))
print('%d * %d = %d' % (a, b, cal1.mul()))


