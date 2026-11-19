class Pet:
    def __init__(self, name: str):
        self.name = name
        self.hunger = 5

    def feed(self, hunger):
        # TODO: Implement this method
        # It should decrease the pet's hunger by 1
        # and print a message about feeding the pet
        for i in range(3):
            self.hunger -= 1
            print(f"{self.name} has been fed.")
            print(f"{self.name}'s hunger level: {self.hunger}")
            

# Create a pet
my_pet = Pet("Fluffy")

# TODO: Feed the pet three times
my_pet.feed(3)