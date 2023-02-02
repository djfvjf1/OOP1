from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, owner, max_speed, weight, number_of_wheels, petrol_type):
        super().__init__()

    def go_straight(self):
        pass

    def go_back(self):
        pass

    def turn_right(self):
        pass

    def turn_left(self):
        pass


class Car(Vehicle):
    def __init__(self, owner, max_speed, weight, number_of_wheels, petrol_type):
        super().__init__(owner, max_speed, weight, number_of_wheels, petrol_type)

    def drive(self):
        print('1: Полный привод\n2: Задний привод\n3: Передний привод')
        d = input()
        if d == '1':
            print('Полный привод')
        elif d == '2':
            print('Задний привод')
        elif d == '3':
            print('Передний привод')

    def fog_lights(self):
        print('противотуманные фары')

car = Car('Misha', '330', '1000 kg', '4', '100')
car.drive()
car.fog_lights()

class Motorcycle(Vehicle):
    def __init__(self, owner, max_speed, weight, number_of_wheels, petrol_type, color):
        super().__init__(owner, max_speed, weight, number_of_wheels, petrol_type)
        self.color = color


    def moto_color(self):
        print(f'{self.color} цвет')

print('\nМотоцикл:')
moto = Motorcycle('Misha', '330', '300 kg', '2', '95', 'Blue')
moto.moto_color()

class Bicycle(Vehicle):
    def __init__(self, owner, max_speed, weight, number_of_wheels, petrol_type, model=[]):
        super().__init__(owner, max_speed, weight, number_of_wheels, petrol_type)
        self.model = model


    def model_of_bike(self):
        print('\nВыберите модель велосипеда:')
        print('1 - BMX, 2 - MTB')

        try:
            a = int(input())
        except:
            print('Выберите числа 1 или 2')

        if a == 1:
            print(self.model[0])
        elif a == 2:
            print(self.model[1])

bike = Bicycle('Misha', '30', '20 kg', '2', 'None', ['BMX', 'MTB'])
bike.model_of_bike()