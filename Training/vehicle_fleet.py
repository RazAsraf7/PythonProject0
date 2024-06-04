class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def toString(self):
        return f"The vehicle is {self.model} by {self.make} "
    
class Car(Vehicle):
    def __init__(self, make, model, number_of_doors):
        super().__init__(make, model)
        self.number_of_doors = number_of_doors

    def toString(self):
        return super().toString() + f"with {self.number_of_doors} doors"
    

class Truck(Vehicle):
    def __init__(self, make, model, payload_capacity):
        super().__init__(make, model)
        self.payload_capacity = payload_capacity
    
    def toString(self):
        return super().toString() + f"with {self.payload_capacity} payload capacity"
    

class Fleet:
    def __init__(self, name):
        self.name = name
        self.vehicles = []

    def addVehicle(self, vehicle_name):
        self.vehicles.append(vehicle_name)

    def listVehicles(self):
        for v in self.vehicles:
            print(v.toString())

    def listCars(self):
        for v in self.vehicles:
            if isinstance(v, Car):
                print(v.toString())

    def listTrucks(self):
        for v in self.vehicles:
            if isinstance(v, Truck):
                print(v.toString())


fleet = Fleet("Tzi Rehev")
car1 = Car("Toyota", "CH-R", 5)
truck1 = Truck("Ford", "F-350 Super Duty", 1500)
fleet.addVehicle(car1)
fleet.addVehicle(truck1)

fleet.listCars()
fleet.listTrucks()
fleet.listVehicles()