# Factory Method
class Car:
    def __init__(self, model):
        self.model = model

    def drive(self):
        print(f"{self.model} is driving")

class CarFactory:
    @staticmethod
    def create_car(car_type):
        if car_type == "Sedan":
            return Car("Sedan")
        elif car_type == "SUV":
            return Car("SUV")
        else:
            return Car("Generic Car")

# Usage
car1 = CarFactory.create_car("Sedan")
car2 = CarFactory.create_car("SUV")
car1.drive()
car2.drive()