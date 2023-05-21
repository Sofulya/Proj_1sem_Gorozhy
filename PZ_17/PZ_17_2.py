# Создание базового класса "Транспортное средство" и его наследование для создания классов "Автомобиль" и "Мотоцикл".
# В классе "Транспортное средство" будут общие свойства, такие как максимальная скорость и количество колес,
# а классы наследники будут иметь свои уникальные свойства и методы.

class Transport:
    def __init__(self, max_speed, num_wheels):
        self.max_speed = max_speed
        self.num_wheels = num_wheels

    def init(self, max_speed, num_wheels):
        pass


class Car(Transport):
    def __init__(self, max_speed, num_wheels, brand, model):
        super().__init__(max_speed, num_wheels)
        super().init(max_speed, num_wheels)
        self.brand = brand
        self.model = model

    def start_engine(self):
        print(
            f"Это {self.brand} {self.model} двигатель работает, её максимальная скорость {self.max_speed}, количество "
            f"колес {self.num_wheels}")


class Motorcycle(Transport):
    def __init__(self, max_speed, num_wheels, brand, model):
        super().__init__(max_speed, num_wheels)
        super().init(max_speed, num_wheels)
        self.brand = brand
        self.model = model

    def wheelie(self):
        print(f"Это {self.brand} {self.model}, его скорость {self.max_speed}, количество колес {self.num_wheels}")


# Создаем объекты классов Car и Motorcycle
my_car = Car(200, 4, "Toyota", "Corolla")
my_motorcycle = Motorcycle(150, 2, "Harley-Davidson", "Sportster")

# Вызываем методы start_engine и wheelie
my_car.start_engine()
my_motorcycle.wheelie()
