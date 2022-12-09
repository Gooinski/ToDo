class Car():
    wheels = 4
    doors = 2
    engine = False

    def __init__(self, model, year, make='Ford'):
        self.make = make
        self.model = model
        self.year = year
        self.gas = 200
        self. is_moving = True

    def __str__(self):
        return f'{self.make}, {self.model}, {self.year}'

    def __eq__(self, other):
        return self.make == other.make and self.model == other.model

    def stop(self):
        if self.is_moving:
            print(f'The {self.model} has stopped')
            self.is_moving = False
        else:
            print(f'The {self.model} is already stopped')        

    def go(self, speed):
        if self.use_gas():
            if not self.is_moving:
                print((f'The {self.model} starts moving'))
                self.is_moving = True
            print(f'The {self.model} is going {speed}')
        else:
            print(f'The {self.model} is out of gas')
            self.stop()

    def use_gas(self):
        self.gas -= 50
        if self.gas <= 0:
            return False
        else:
            return True



class Dealership:
    def __init__(self):
        self.cars = []

    def __iter__(self):
        yield from self.cars

    def add_car(self, car):
        self.cars.append(car)


car_one = Car('Model T', 1908)
car_two = Car('Phantom', 2020, 'Rolls Royce')
car_three = Car('Fusion', 1990)
car_four = Car('Fiesta', 2000)
car_five = Car('Fiesta', 2001)

my_dealship = Dealership()

my_dealship.add_car(car_one)
my_dealship.add_car(car_two)
my_dealship.add_car(car_three)
my_dealship.add_car(car_four)

for car in my_dealship:
    print(car)

#output

print(f'car_one {car_one.make}')
print(f'car_two {car_two.make}')

car_one.year = 1980

print(f'car_one {car_one.year}')

print(car_one.__dict__)

car_one.stop()
print(f'Is {car_one.model} moving? {car_one.is_moving}')

car_one.go('fast')
car_one.go('slow')

print(f'Is {car_one.model} moving? {car_one.is_moving}')

car_one.go('slow')
car_one.go('slow')

print(f'Is {car_one.model} moving? {car_one.is_moving}')

if car_four == car_five:
    print('Cars are equal make and model')
else:
    print('Cars are not equal make and model')