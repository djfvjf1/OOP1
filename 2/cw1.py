class Animal:
    def __init__(self, food, location):
        self.food = food
        self.location = location

    def make_noise(self):
        print('Animal is sleeping')

    def eat(self):
        print(self.food)

    def sleep(self):
        print(self.location)

class Dog(Animal):
    def __init__(self, food, location, name):
        super().__init__(food, location)
        self.name = name

    def make_noise(self):
        print("GAV GAV")

    def eat(self):
        print('bones')

    def gabarite(self):
        print('big')

class Cat(Animal):
    def __init__(self, food, location, name):
        super().__init__(food, location)
        self.name = name

    def make_noise(self):
        print("GAV GAV")

    def eat(self):
        print('bones')

    def gabarite(self):
        print('small')

class Boozer(Animal):
    def __init__(self, food, location, name):
        super().__init__(food, location)
        self.name = name
        
    def make_noise(self):
        print("UAUAUAUAUAUA")
    
    def eat(self):
        print('vodka')

    def get_name(self):
        print('Valera')


class Vet:
    def treat_animal(self, animal):
        print(animal.food, animal.location)

a1 = Dog('bones', 'Street', 'Sharik')
a2 = Cat('fish', 'Street', 'Barsik')
a3 = Boozer('vodka', 'Street', 'Valera')
a = [a1,a2,a3]

vet = Vet()

for i in range(len(a)):
    vet.treat_animal(a[i])


    


    
    