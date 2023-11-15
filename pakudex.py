from pakuri import Pakuri
class Pakudex:
    def __init__(self, capacity = 20): # sets a default capcity
        self.capacity = int(capacity) # initial value is 20
        self.pakuris = [] # store a list of pakuri objects
        self.size = int(0) # keep track # of concrete pakuri objects in self.pakuris

    def get_size(self):
        return self.size # returns size

    def get_capacity(self):
        return self.capacity # returns capacity

    def get_species_array(self):
        res = [] # creates a list
        count = 0 # creates a count

        for pakuri in self.pakuris: # loop through self.pakuris to look at each pakuri object
            res.append(pakuri.get_species()) # append pakuri.species to the res list
            count += 1 # adds to count

        if count == 0: # check if there's nothing added
            print("No Pakuri in Pakudex yet!") # prints error message
            return None # returns as None

        else:
            print(f"Pakuri In Pakudex:") # prints start
            count = 0 # sets count value
            for pakuri in res[::]: # goes through the items in the res list
                count += 1 # adds to count
                print(f"{count}. {pakuri}") # prints the count with the corresponding list item
            return res # returns list

    def get_stats(self, species):
        stat = [] # creates stat list

        for item in self.pakuris: # loop through self.pakuris to look at each pakuri object

            if item.get_species() == species: # compare pakuri.species == species
                stat.append(item.get_attack()) # adds attack value to stat list
                stat.append(item.get_defense()) # adds defense value to state list
                stat.append(item.get_speed()) # adds speed valie to stat list
                print(f"Species: {species}\nAttack: {stat[0]}\nDefense: {stat[1]}\nSpeed: {stat[2]}") # prints out collected infromation
                return stat # if true, return [pakuri.attack, pakuri.defense, pakuri.speed]

        print("Error: No such Pakuri!") # prints error message
        return None

    def sort_pakuri(self): # sorts pakuri objects in pakudex according to Python lxicographical ordering
        print("Pakuri have been sorted!")
        return self.pakuris.sort() # sorts Pakuri list

    def add_pakuri(self, species): # species vs. pakuri object

        # 1. check duplicates => return False
        for item in self.pakuris: # loop through self.pakuris to look at each pakuri object

            if item.get_species() == species: # compare pakuri.species == species
                print("Error: Pakudex already contains this species!") # prints error message
                return False

        if self.get_size() == self.get_capacity(): # checks size vs. capacity
            print("Error Pakudex is full!") # prints error message
            return False

            # 2. when the list is full => return False
        new_pakuri = Pakuri(str(species)) # creates object
        self.pakuris.append(new_pakuri) # add a new pakuri object into the list
        self.size += 1 # increment self.size
        print(f"Pakuri species {species} successfully added!") # prints success message
        return True

    def evolve_species(self, species):

        for item in self.pakuris: # loops through pakuri list

            if item.get_species() == species: # checks object vs. species
                item.evolve() # evolves species stats
                print(f"{species} has evolved!") # prints success message
                return True

        print("Error: No such Pakuri!") # prints error message
        return False