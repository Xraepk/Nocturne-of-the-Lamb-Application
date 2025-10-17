
def main():
    #Imports
    import os
    import random



    #Constants, Defaults
    DEFAULT_ROOMS = ["Sanctuary", "Kitchen", "Parish Hall", "Confessionals", "Crypt", "Bell Tower", "Pastor's Study"]
    DEFAULT_NPC_LIST = ["Clara", "Jacob", "Janice", "Carter", "Lola", "Walter",
                        "Nora", "Shawn", "Helen", "Lewis", "Violet", "Brad"]
    DEFAULT_NPC_ATTRIBUTES = {
                            "Hair Lengths": {"Short": 35, "Medium": 20, "Long": 45},
                            "Hair Colors": {"Blond": 30, "Brown": 40, "Black": 25},
                            "Shoe Types": {"Sneakers": 40, "Boots": 30, "Sandals": 30}
                            "Outer Wear": {"Hoodie": 35, "Cardigan": 25, "None": 40}
                            "Shirt Colors": {"Black": 20, "Blue": 20, "Grey": 20, "Green": 10, "Red": 20, "Yellow": 10}
                            "Pants Types": {"Jeans": 35, "Slacks": 35, "Sweat Pants": 30}
                            ""
                             }

    #Variables
    user_name = ""
    user_info = ""
    killer = ""

    #Functions
    def wipe():
        os.system('cls' if os.name == 'nt' else 'clear')

    def settings():
        return None

    def custom_presets():
        return None

    def intro_sequence():
        wipe()
        global user_name
        global user_info
        intro_over = False

        while intro_over == False:
            name_accepted = False
            has_account = input("Do you have an account? (Y/N): ")
            if has_account.upper() == "Y":
                while name_accepted == False:
                    user_name = input("\nPlease enter your Username or enter \"R\" to return: ").upper().strip()
                    if user_name == "R":
                        print("\n...Redirecting...\n")
                        name_accepted = True
                    elif os.path.exists(user_name) and os.path.isfile(user_name):
                        user_file = open(user_name, "r+")
                        user_info = user_file.readlines()
                        user_file.close()
                        print(f"\nLogin Successful. Welcome {user_name.title()}! (Enter anything to continue)", end=" ")
                        name_accepted = True
                        intro_over = True
                    else:
                        print("\nUsername not found in system.\n")
            elif has_account.upper() == "N":
                while name_accepted == False:
                    user_name = input("\nPlease enter a new Username or enter \"R\" to return: ").upper().strip()
                    if user_name == "R":
                        print("\n...Redirecting...\n")
                        name_accepted = True
                    elif not(os.path.exists(user_name) or os.path.isfile(user_name)):
                        user_file = open(user_name, "w")
                        user_file.close()
                        name_accepted = True
                    else:
                        print("\nCannot re-write a pre-existing file. Please try a different Username.")
            else:
                print("\nAnswer must be either \"Y\" or \"N\".\n")
        input()
        wipe()

    def start_screen():
        begin = False
        while begin == False:
            nav_code = input("Enter \"ST\" to start, \"SE\" to edit settings, or \"P\" to create custom presets: ")
            nav_code = nav_code.upper()
            if nav_code == "ST":
                begin = True
            elif nav_code == "SE":
                settings()
            elif nav_code == "P":
                custom_presets()
            else:
                print("Input must be \"ST\", \"SE\", or \"P\".\n")

    def generate(rooms=DEFAULT_ROOM_LIST, NPCs=DEFAULT_NPC_LIST):
        global killer
        killer = random.choice(NPCs)
        print()
        print(killer)



    intro_sequence()
    start_screen()
    generate()


if __name__ == '__main__':
    main()