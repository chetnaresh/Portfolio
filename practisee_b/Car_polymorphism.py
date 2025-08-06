class Car:
    def __init__(self, speed, fuel, distance=0):
        self.speed = speed
        self.fuel = fuel
        self.distance = distance

    def drive(self, hours):
        print("Driving a fuel-based car...")
        self.distance += self.speed * hours
        self.fuel -= hours * 5
        print(f"Distance: {self.distance}, Fuel: {self.fuel}")

class ElectricCar:
    def __init__(self, speed, battery, distance=0):
        self.speed = speed
        self.battery = battery
        self.distance = distance

    def drive(self, hours):
        print("Driving an electric car...")
        self.distance += self.speed * hours
        self.battery -= hours * 10
        print(f"Distance: {self.distance}, Battery: {self.battery}")


obj1 = Car(60,50)
obj2=ElectricCar(70,100)
obj1.drive(2)
obj2.drive(2)


