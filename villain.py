villain.py

class Villain:
    def __init__(self, name, evil_level=80):
        
        self.name = name
        self._evil_level = evil_level
        self.flight_power = True

    def fly(self):
        print(f"{self.name} is flying menacingly!")

    def use_power(self):
        print(f"{self.name} uses their villainous power!")


class ZMan(Villain):
    def __init__(self, name, weapon="Dark Energy", evil_level=100):
        super().__init__(name, evil_level)
        self.weapon = weapon

    def use_power(self):
        super().use_power()
        print(f"{self.name} uses their flight power to outmaneuver the hero.")

    def attack(self):
        
        print(f"{self.name} attacks using {self.weapon}!")



z_man_villain = ZMan("Z-Man")
