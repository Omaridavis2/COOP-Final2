hero.py

class Superhero:
    def __init__(self, name, power_level=100):
        
        self.name = name
        
        self._power_level = power_level
        
        self.flight_power = True

    def fly(self):
        
        print(f"{self.name} is soaring through the sky!")

    def use_power(self):
       
        print(f"{self.name} uses their superpower!")


class Spartan(Superhero):
    def __init__(self, name, weapon="Sword", power_level=120):
        
        super().__init__(name, power_level)
        
        self.weapon = weapon

    def use_power(self):
        
        super().use_power()
        print(f"{self.name} uses their flight power to maneuver quickly.")

    def attack(self):
        
        print(f"{self.name} attacks using {self.weapon}!")



spartan_hero = Spartan("Spartan")
