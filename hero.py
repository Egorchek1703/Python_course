
class Heroes():
    def __init__(self, name, lvl, race, power):
        self.name = name
        self.lvl = lvl
        self.race = race
        self.power = power
        self.health = 100

    def show_hero_desc(self):
        description = self.name + " is a " + self.race + " and has:\n\tlevel: " + str(self.lvl) + "\n\tpower: " + str(self.power) 
        print(description)

    def increase_lvl(self):
        self.lvl += 1

    def train_hero(self):
        print(self.name + ' has just started training')

    def set_new_health(self, new_health):
        self.health = new_health


class Orcs (Heroes):
    def __init__(self, name, lvl, race, power, armor_lvl):
        super().__init__(name, lvl, race, power)
        self.armor_lvl = armor_lvl
    
    def show_hero_desc(self):
        description = self.name + " is a " + self.race + " and has:\n\tlevel: " + str(self.lvl) + "\n\tpower: " + str(self.power) + "\n\tarmor_level: " + str(self.armor_lvl)
        print(description)