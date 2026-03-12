from abc import ABC, abstractmethod

class Car(ABC):
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color

    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

class CombustionCar(Car):
        def start_engine(self):
            print(f'{self.brand} {self.model} engine started.')

        def stop_engine(self):
            print(f'{self.brand} {self.model} engine stopped.')

class ElectricCar(Car):
        def __init__(self, brand, model, color, battery_capacity):
            super().__init__(brand, model, color)
            self.battery_capacity = battery_capacity
        def start_engine(self):
            print(f'{self.brand} {self.model} electric motor started.')

        def stop_engine(self):
            print(f'{self.brand} {self.model} electric motor stopped.')


if __name__ == '__main__':
    combustion_car = CombustionCar('Toyota', 'Corolla', 'Red')
    electric_car = ElectricCar('Tesla', 'Model 3', 'Blue', 75)

    combustion_car.start_engine()
    combustion_car.stop_engine()

    electric_car.start_engine()
    electric_car.stop_engine()
