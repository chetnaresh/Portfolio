class Car:
    def __init__(self, speed, fuel, distance=0):
        self.speed = speed
        self.fuel = fuel
        self.distance = distance

    def drive(self, hours):
        possible_distance = self.speed * hours
        fuel_needed = hours * 5

        if self.fuel >= fuel_needed:
            self.distance += possible_distance
            self.fuel -= fuel_needed
            print(f"Driven {possible_distance} km. Fuel left: {self.fuel}")
        else:
            print("Not enough fuel.")

class ElectricCar(Car):
    def __init__(self, speed, battery, distance=0):
        super().__init__(speed, fuel=battery, distance=distance)

c1 = Car(60, 50)
e1 = ElectricCar(70, 100)

c1.drive(2) 
e1.drive(3)   
