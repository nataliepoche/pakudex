class Pakuri:
    def __init__(self, species): # sets object
        self.species = species
        self.attack = (len(species) * 7) + 9
        self.defense = (len(species) * 5) + 17
        self.speed = (len(species) * 6) + 13

    # getters and setters
    def get_species(self): # getters: retrieve the value of an attribute
        return self.species

    def get_attack(self):
        return self.attack

    def get_defense(self):
        return self.defense

    def get_speed(self):
        return self.speed

    def set_attack(self, new_attack): # setters: set the value of a specific attribute
        self.attack = new_attack # do not want to return anything in the setters, want to update

    def evolve(self): # update self.attack, self.defense, self.speed
        self.attack = self.attack * 2
        self.defense = self.defense * 4
        self.speed = self.speed * 3

    def __lt__(self, other): # want to sort
        return self.species < other.species
        # self.attack <= other.attack, based on value