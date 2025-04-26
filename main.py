# main.py
from pet import Pet

# Create a pet
my_pet = Pet("Max")

# Interact with the pet
my_pet.eat()
my_pet.play()
my_pet.sleep()
my_pet.train("roll over")
my_pet.train("play dead")

# Show current status
my_pet.get_status()
my_pet.show_tricks()
