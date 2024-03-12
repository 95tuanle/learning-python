class Vehicle:
    def __init__(self, body_style):
        self.speed = None
        self.mode = None
        self.body_style = body_style

    def drive(self, speed):
        self.mode = "driving"
        self.speed = speed


class Car(Vehicle):
    def __init__(self, engine_type):
        super().__init__("Car")
        self.engine_type = engine_type
        self.wheels = 4
        self.doors = 4

    def drive(self, speed):
        super().drive(speed)
        print("Driving my", self.engine_type, "car at", self.speed, "mph")


class Motorcycle(Vehicle):
    def __init__(self, engine_type, side_car):
        super().__init__("Motorcycle")
        self.engine_type = engine_type
        if side_car:
            self.wheels = 3
        else:
            self.wheels = 2
        self.doors = 0

    def drive(self, speed):
        super().drive(speed)
        print("Driving my", self.engine_type, "motorcycle at", self.speed, "mph")


car1 = Car("gas")
car2 = Car("electric")
mc1 = Motorcycle("gas", True)

print(car1.engine_type)
print(car2.doors)
print(mc1.wheels)

car1.drive(30)
car2.drive(40)
mc1.drive(50)
