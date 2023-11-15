from pakudex import Pakudex

def main():
    # prints start
    print("Welcome to Pakudex: Tracker Extraordinaire!")
    capacity = input("Enter max capacity of the Pakudex: ")

    while not capacity.isnumeric():
        print("Please enter a valid size.")
        capacity = input("Enter max capacity of the Pakudex: ")

    # prints menu
    print(f"The Pakudex can hold {capacity} species of Pakuri.")
    print("Pakudex Main Menu")
    print("-" * 17)
    print("1. List Pakuri\n2. Show Pakuri\n3. Add Pakuri\n4. Evolve Pakuri \n5. Sort Pakuri\n6. Exit")

    choice = input("What would you like to do?")
    pakudex = Pakudex(capacity)

    if choice == "1":  # List pakuri
        pakudex.get_species_array() # checks list and prints list

    elif choice == "2":  # Show pakuri
        species = input("Enter the name of the species to display: ") # asks for species
        pakudex.get_stats(species) # checks species and gets species details

    elif choice == "3":  # Add pakuri
        species = input("Enter the name of the species to add: ") # asks for species
        pakudex.add_pakuri(species) # checks list for current species then adds species

    elif choice == "4":  # Evolve pakuri
        species = input("Enter the name of the species to evolve: ") # asks for species
        pakudex.evolve_species(species) # checks list and evolves species

    elif choice == "5":  # Sort pakuri
        pakudex.sort_pakuri() # sorts list

    elif choice == "6":  # Exit
        print("Thanks for using Pakudex! Bye!") # prints exist statement
        choice = "6" # exists program

    else:
        print("Unrecognized menu selection!") # choice error statement

    while choice != "6": # starts loop
        # prints menu selection
        print("Pakudex Main Menu")
        print("-" * 17)
        print("1. List Pakuri\n2. Show Pakuri\n3. Add Pakuri\n4. Evolve Pakuri \n5. Sort Pakuri\n6. Exit")
        choice = input("What would you like to do?")

        if choice == "1":  # List pakuri
            pakudex.get_species_array()  # checks list and prints list

        elif choice == "2":  # Show pakuri
            species = input("Enter the name of the species to display: ")  # asks for species
            pakudex.get_stats(species)  # checks species and gets species details

        elif choice == "3":  # Add pakuri
            if pakudex.get_size() == pakudex.get_capacity(): # checks for capacity
                print("Error: Pakudex is full!") # prints capacity statment
                continue # continues to new choice
            species = input("Enter the name of the species to add: ")  # asks for species
            pakudex.add_pakuri(species)  # checks list for current species then adds species

        elif choice == "4": # Evolve pakuri
            species = input("Enter the name of the species to evolve: ")  # asks for species
            pakudex.evolve_species(species)  # checks list and evolves species

        elif choice == "5": # Sort pakuri
            pakudex.sort_pakuri() # sorts list

        elif choice == "6": # Exit
            print("Thanks for using Pakudex! Bye!")  # prints exist statement
            choice = "6"  # exists program

        else:
            print("Unrecognized menu selection!") # choice error statment

if __name__ == "__main__":
    main()