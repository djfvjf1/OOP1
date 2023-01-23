class Phone:
    def __init__(self, number, model, weight):
        self.number = number
        self.model = model
        self.weight = weight

    def receive_call(self, name):
        return name
    
    def get_number(self):
        return self.number

    def all_info(self):
        return self.number, self.model, self.weight

p1 = Phone(87777777777, 'Samsung', 250)
#print(p1.number, p1.model, p1.weight)
print(p1.all_info())

p2 = Phone(87777777777, 'Samsung', 250)
print(p1.receive_call('Misha'))

p3 = Phone(87777777777, 'Samsung', 250)
print(p1.get_number())



class Calc:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def power(self):
        return self.a ** self.b

c1 = Calc(2, 4)
print(c1.power())


class Matrix:
    def __init__(self, arr1):
        self.arr1 = arr1
        

    def Sum(self, arr2):

        self.c = [[0,0,0],[0,0,0],[0,0,0]]
        for i in range(len(self.arr1)):
            for j in range(len(self.arr1)):
                self.c[i][j] = self.arr1[i][j] + arr2[i][j]
        for i in range(len(self.c)):
            print(self.c[i])

a = [[int(x) for x in input().split()] for i in range(3)]
b = [[int(x) for x in input().split()] for i in range(3)]

m = Matrix(a)
m.Sum(b)