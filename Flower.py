# Author: Muaiwyah Ayyub		
# Date: 11/4/2023
# Purpose: This code defines a Flower class and creates two Flower objects. The Flower class has an attribute "name" and two methods, "grow" and "bloom."

# Define the Flower class
class Flower:
    # Constructor to initialize the name attribute
    def __init__(self, name):
        self.name = name

    # Method to make the flower grow
    def grow(self):
        print(f"{self.name} is growing.")

    # Method to make the flower bloom
    def bloom(self):
        print(f"{self.name} is blooming.")

# Create two Flower objects with names
flower1 = Flower("Rose")
flower2 = Flower("Tulip")

# Call methods on the Flower objects
flower1.grow()
flower1.bloom()
flower2.grow()
flower2.bloom()

# Create another Flower object of your choice (let's say "Daisy")
flower3 = Flower("Daisy")

# Call methods on the new Flower object
flower3.grow()
flower3.bloom()

