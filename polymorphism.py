# Base class
class Vehicle:
    def move(self):
        print("This vehicle moves.")

# Subclass 1
class Car(Vehicle):
    def move(self):
        print("The car drives on the road. 🚗")

# Subclass 2
class Plane(Vehicle):
    def move(self):
        print("The plane flies in the air. ✈️")

# Subclass 3
class Bicycle(Vehicle):
    def move(self):
        print("The bicycle pedals along the path. 🚴")

# Polymorphic behavior
vehicles = [Car(), Plane(), Bicycle()]

for v in vehicles:
    v.move()
