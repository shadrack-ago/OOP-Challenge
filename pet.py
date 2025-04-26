# pet.py
class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []

    def eat(self):
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)
        print(f"{self.name} is eating 🍽️...")

    def sleep(self):
        self.energy = min(10, self.energy + 5)
        print(f"{self.name} is sleeping 💤...")

    def play(self):
        if self.energy >= 2:
            self.energy = max(0, self.energy - 2)
            self.happiness = min(10, self.happiness + 2)
            self.hunger = min(10, self.hunger + 1)
            print(f"{self.name} is playing 🎾...")
        else:
            print(f"{self.name} is too tired to play 😴! Sleeping first...")
            self.sleep()
            self.play()

    def train(self, trick):
        self.tricks.append(trick)
        print(f"{self.name} learned a new trick: {trick} 🎓")

    def show_tricks(self):
        if self.tricks:
            print(f"{self.name}'s tricks: {', '.join(self.tricks)}")
        else:
            print(f"{self.name} hasn't learned any tricks yet.")

    def get_status(self):
        print(f"\n{self.name}'s Current Status 📋:")
        print(f"Hunger: {self.hunger}")
        print(f"Energy: {self.energy}")
        print(f"Happiness: {self.happiness}")
        print(f"Tricks: {self.tricks}\n")
