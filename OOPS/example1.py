#Code to create a class named Vehicle which has objects like number of wheels, color, and type. The class should have a method to display the details of the vehicle.
class Vehicle:
    def __init__(self, wheels, color, vehicle_type):
        self.wheels = wheels
        self.color = color
        self.vehicle_type = vehicle_type    
    def display_details(self):
        print(f"Vehicle Details:")
        print(f"Number of Wheels: {self.wheels}")
        print(f"Color: {self.color}")
        print(f"Type: {self.vehicle_type}") 
my_vehicle = Vehicle(4, "Red", "Car")
my_vehicle.display_details()
