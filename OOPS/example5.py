class Distance:
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches
    def display(self):
        print(f"Distance: {self.feet} feet {self.inches} inches")
    def __add__(self, other):
        total_feet = self.feet + other.feet
        total_inches = self.inches + other.inches
        # Convert inches to feet if total inches exceed 12
        if total_inches >= 12:
            total_feet += total_inches // 12
            total_inches = total_inches % 12
        return Distance(total_feet, total_inches)
    def __str__(self):
        return f"{self.feet} feet {self.inches} inches"
distance1 = Distance(5, 8)  
distance2 = Distance(3, 10)
print("Distance 1:", distance1)
print("Distance 2:", distance2)
total_distance = distance1 + distance2
print("Total Distance:", total_distance)
