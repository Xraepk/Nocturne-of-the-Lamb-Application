
def main():
    #Imports
    import os
    import random



    #Constants, Defaults
    DEFAULT_ROOMS = ["Sanctuary", "Kitchen", "Parish Hall", "Confessionals", "Crypt", "Bell Tower", "Pastor's Study"]
    DEFAULT_NPC_LIST = ["Clara", "Jacob", "Janice", "Carter", "Lola", "Walter",
                        "Nora", "Shawn", "Helen", "Lewis", "Violet", "Brad"]

    #The following attributes are definitive and must be included in any preset. You can change the types, as in making
    #hair colors red, blue and green, but hair colors must be included. The numbers beside the defaults are optional
    #percentages for how likely it is that a character will have each attribute. Can be turned off for even spreading.

    DEFAULT_NPC_ATTRIBUTES = {
                            "Hair Lengths": ["Short", "Medium", "Long"],
                            "Hair Colors": ["Blond", "Brown", "Black"],
                            "Shoe Types": ["Sneakers", "Boots", "Sandals"],
                            "Outer Wear": ["Hoodie", "Cardigan", "None"],
                            "Shirt Colors": ["Black", "Blue", "Grey", "Green", "Red", "Yellow"],
                            "Pants Types": ["Jeans", "Slacks""Sweat Pants"],
                            #By default there will be a 50% chance of there being no special wear or items on an NPC.
                            "Special Wear": { "Glasses": ["Has them", "Does not have them"], "Jewelry": ["Bracelet", "Necklace", "Anklet"]},
                            "Special Items": ["Bible", "Flashlight"]
                            }


    #Variables
    user_name = ""
    user_info = ""
    killer = ""
    rooms = DEFAULT_ROOMS
    npc_list = DEFAULT_NPC_LIST
    npc_attributes = DEFAULT_NPC_ATTRIBUTES

    #Functions
    def wipe():
        os.system('cls' if os.name == 'nt' else 'clear')

    def settings():
        return None

    def write_preset(name, rooms=DEFAULT_ROOMS, npc_list=DEFAULT_NPC_LIST, attributes=DEFAULT_NPC_ATTRIBUTES, new_write=True):
        global user_name
        if new_write:
            with open(user_name, "a+") as user_file:
                user_file.write(name)
        with open(name, "w") as new_preset_file:
            for index, room in enumerate(rooms):
                if index != len(rooms) - 1:
                    new_preset_file.write(f"{room}, ")
                else:
                    new_preset_file.write(str(room))
            new_preset_file.write("\n")
            for index, npc in enumerate(npc_list):
                if index != len(npc_list) - 1:
                    new_preset_file.write(f"{npc}, ")
                else:
                    new_preset_file.write(str(npc))
            new_preset_file.write("\n")
            new_preset_file.write(str(attributes))
        print("\nFile Updated\n")

    def read_preset(name):
        global rooms, npc_list, attributes
        with open(name, "r") as current_file:
            current_info = current_file.readlines()
        rooms = current_info[0].split(",")
        npc_list = current_info[1].split(",")
        attributes = current_info[2].split(",")
        wipe()
        print(f"{name} file info: ")
        print("\n\tRooms:", end=" ")
        for index, room in enumerate(rooms):
            if index == len(rooms) - 1:
                print(room, end="")
            else:
                print(room, end=", ")
        print()
        print("\n\tNPC List:", end=" ")
        for index, room in enumerate(npc_list):
            if index == len(npc_list) - 1:
                print(room, end="")
            else:
                print(room, end=", ")
        print()
        print("\n\tNPC Attributes:", end=" ")
        for index, room in enumerate(npc_attributes):
            if index == len(npc_attributes) - 1:
                print(room, end="")
            else:
                print(room, end=", ")
        print()

    def edit_preset():
        edit_over = False
        while edit_over == False:
            global user_name
            current_preset_name = input("\nEnter the name of the file you wish to inspect or enter \"R\" to return: ").strip()
            with open(user_name, "r+") as preset_file:
                preset_info = preset_file.readlines()
                if current_preset_name.strip().upper() == "R":
                    edit_over = True
                elif current_preset_name in preset_info:
                    read_preset(current_preset_name)
                    #The Actual edit actions
                    changing_preset = True

                    new_rooms = rooms
                    new_npc_list = npc_list
                    new_npc_attributes = npc_attributes
                    print("\nEnter one of the following keywords to edit your preset: ")
                    print("\t\"A\" - Room list")
                    print("\t\"B\" - NPC name list")
                    print("\t\"C\" - Attribute list")
                    print("Enter anything else to return")
                    edit_nav = input("Enter: ").strip().upper()

                    if edit_nav == "A":
                        editing_rooms = True
                        wipe()
                        print(f"Enter room names one at a time. Enter \"Done\" when you have finished entering names.\n")
                        new_rooms = []
                        while editing_rooms == True:
                            room_name = input("Enter: ").strip().title()
                            if room_name == "Done":
                                print("Changed Room List: ", end="")
                                for index, room in enumerate(new_rooms):
                                    if index == len(new_rooms) - 1:
                                        print(room, end="")
                                    else:
                                        print(room, end=", ")
                                finalize_nav = input("\nDo you want to re-write rooms for this preset? (Y/N): ").strip().upper()
                                if finalize_nav == "Y":
                                    write_preset(current_preset_name, new_rooms, new_npc_list, new_npc_attributes, False)
                                elif finalize_nav == "N":
                                    print("\n...Redirecting...\n")
                                editing_rooms = False
                            else:
                                new_rooms.append(room_name)

                    elif edit_nav == "B":
                        editing_npc_list = True
                        wipe()
                        print(f"Enter NPC names one at a time. Enter \"Done\" when you have finished entering names.\n")
                        new_npc_list = []
                        while editing_npc_list == True:
                            room_name = input("Enter: ").strip().title()
                            if room_name == "Done":
                                print("Changed Room List: ", end="")
                                for index, room in enumerate(new_npc_list):
                                    if index == len(new_npc_list) - 1:
                                        print(room, end="")
                                    else:
                                        print(room, end=", ")
                                finalize_nav = input(
                                    "\nDo you want to re-write rooms for this preset? (Y/N): ").strip().upper()
                                if finalize_nav == "Y":
                                    write_preset(current_preset_name, new_rooms, new_npc_list, new_npc_attributes,False)
                                elif finalize_nav == "N":
                                    print("\n...Redirecting...\n")
                                editing_npc_list = False
                            else:
                                new_npc_list.append(room_name)

                    elif edit_nav == "C":
                        editing_attributes = True
                        wipe()
                        while editing_attributes == True:
                            print("\nEnter one of the following keywords to edit your attributes: ")
                            print("\t\"A\" - Hair Lengths")
                            print("\t\"B\" - Hair Colors")
                            print("\t\"C\" - Shoe Types")
                            print("\t\"D\" - Outer Wear")
                            print("\t\"E\" - Shirt Colors")
                            print("\t\"F\" - Pants Types")
                            print("\t\"G\" - Special Wear")
                            print("\t\"H\" - Special Items")
                            print("Enter anything else to return")

                    else:
                        print()



                else:
                    print("\nFile name not recognized. Try again.")

    def custom_presets():
        wipe()
        create_over = False
        name_accepted = False
        global user_name
        with open(user_name, "r+") as presets:
            preset_info = presets.readlines()
            print("These are the presets currently active on this account:")
            print(f"\n\t Nocturne of the Lamb (Default)")
            for line in preset_info:
                print(f"\t", line)
            while create_over == False:
                preset_nav_code = input(f"\nEnter \"C\" to create a new preset, enter \"E\" to edit, or enter anything else to return. ")
                if preset_nav_code.strip().upper() == "C":
                    while name_accepted == False:
                        preset_name = input("\nEnter the name of your new preset file: ")
                        if os.path.exists(preset_name) or os.path.isfile(preset_name):
                            print("\nCannot re-write a pre-existing file. Please try a different file name.\n")
                        else:
                            write_preset(preset_name)
                            name_accepted = True
                elif preset_nav_code.strip().upper() == "E":
                        edit_preset()
                else:
                    create_over = True

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
            wipe()
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

    def generate(NPCs=DEFAULT_NPC_LIST):
        global killer
        killer = random.choice(NPCs)
        print()
        print(killer)



    intro_sequence()
    start_screen()
    generate()


if __name__ == '__main__':
    main()