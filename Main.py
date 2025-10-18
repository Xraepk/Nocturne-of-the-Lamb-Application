
def main():
    #Imports
    import os
    import random



    #Constants, Defaults

    DEFAULT_ROOMS = {
                        "Sanctuary" : "A large open room with rows of pews lining the carpeted floors.",
                        "Kitchen" : """A comfortably sized room with cooking equipment lining the walls and a central
counter poking up through the tiled floors""",
                        "Parish Hall" : """A large open room designed for children with a few tables for potlucks and
games on top of the colorful carpet patterns of the floor.""",
                        "Confessionals" : """A small room with two identical boxes placed at the end, made for
confessing sins, with a hole between then for secret listening.""",
                        "Crypt" : """A dark room where the bodies of previous pastors lay, watching over the future of
St.Jude's. The electric box is located here.""",
                        "Bell Tower" : """A winding staircase that leads to an open area with dangerously low railing
and the church's bell.""",
                        "Pastor's Study" : """A small room similar to a library, with a desk in the center ad all
sorts of books pertaining to religious doctrine"""
                    }
    #This list will eventually be turned into a dict on generation where each NPC's value is their attributes.
    #May use named tuple for that. Haven't decided yet.
    DEFAULT_NPC_LIST = ["Clara", "Jacob", "Janice", "Carter", "Lola", "Walter",
                        "Nora", "Shawn", "Helen", "Lewis", "Violet", "Brad"]

    #The following attributes are definitive and must be included in any preset. You can change the types, as in making
    #hair colors red, blue and green, but hair colors must be included. The numbers beside the defaults are optional
    #percentages for how likely it is that a character will have each attribute. Can be turned off for even spreading.

    DEFAULT_NPC_ATTRIBUTES = {
"Hair Lengths":["Short,Medium,Long"],
"Hair Colors":["Blond,Brown,Black"],
"Shoe Types":["Sneakers,Boots,Sandals"],
"Outer Wear":["Hoodie,Cardigan,None"],
"Shirt Colors":["Black,Blue,Grey,Green,Red,Yellow"],
"Pants Types":["Jeans,Slacks,Sweat Pants"],
"Special Wear":["Glasses,Jewelry"],
"Special Items":["Bible,Flashlight"]
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

    def print_preset_names():
        wipe()
        global user_name
        with open(user_name, "r") as presets:
            preset_info = presets.readlines()
            print("These are the presets currently active on this account:")
            print(f"\n\t Nocturne of the Lamb (Default)")
            for line in preset_info:
                print(f"\t", line)

    def settings():
        return None

    def write_preset(name, func_rooms=DEFAULT_ROOMS, npc_list=DEFAULT_NPC_LIST, attributes=DEFAULT_NPC_ATTRIBUTES, type="new"):
        global user_name
        if type == "new":
            with open(user_name, "a+") as user_file:
                user_file.write("\n")
                user_file.write(name)
        with open(name, "w") as new_preset_file:
            for index, room in enumerate(func_rooms):
                if index != len(func_rooms) - 1:
                    new_preset_file.write(f"{room}, ")
                else:
                    new_preset_file.write(str(room))
            if type == "room" or type == "new":
                new_preset_file.write("\n")
            for index, npc in enumerate(npc_list):
                if index != len(npc_list) - 1:
                    new_preset_file.write(f"{npc}, ")
                else:
                    new_preset_file.write(str(npc))
            if type == "npc" or type == "new":
                new_preset_file.write("\n")
            attributes = dict(attributes)
            new_attribute_list = []
            for item, attribute in attributes.items():
                val = ""
                if type == "new":
                    for word in str(attribute).split(","):
                        val += f"{word},"
                    val = val[:-1]
                    new_attribute_list.append(f"  {item}:{val},")
                else:
                    val += "  "
                    for word in attribute:
                        val += f"{word},"
                    val += " "
                    new_attribute_list.append(f"{item}:{val},")
            new_preset_file.write(f"{"/".join(new_attribute_list)[:-1]}")
        input("\nFile Updated. (Enter) ")

    def read_preset(name):
        with open(name, "r") as current_file:
            current_info = current_file.readlines()
        rooms = current_info[0].split(",")
        npc_list = current_info[1].split(",")

        npc_attributes = {}
        attribute_info = current_info[2].split(",/")
        for section in attribute_info:
            parts = section.split(":")[:]
            val = parts[1][2:-2].split(",")
            npc_attributes[parts[0]] = val
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
        for index, npc in enumerate(npc_list):
            if index == len(npc_list) - 1:
                print(npc, end="")
            else:
                print(npc, end=", ")
        print()
        print("\n\tNPC Attributes:")
        for key, val in npc_attributes.items():
            print(f"{key} : {val}")
        print()
        return rooms, npc_list, npc_attributes

    def edit_preset():
        global user_name
        current_preset_name = input("\nEnter the name of the file you wish to inspect or enter \"R\" to return: ").strip()
        with open(user_name, "r+") as preset_file:
            preset_info = preset_file.readlines()
            if current_preset_name.strip().upper() == "R":
                edit_over = True
                print_preset_names()
            elif current_preset_name in preset_info:
                rooms, npc_list, npc_attributes = read_preset(current_preset_name)
                #The Actual edit actions
                changing_preset = True

                new_rooms = rooms
                new_npc_list = npc_list
                new_npc_attributes = npc_attributes
                print("\nEnter one of the following keywords to edit your preset: ")
                print("\t\"A\" - Room list")
                print("\t\"B\" - NPC name list")
                print("\t\"C\" - Attribute list")
                print("\tEnter anything else to return")
                edit_nav = input("Enter: ").strip().upper()

                if edit_nav == "A":
                    editing_rooms = True
                    wipe()
                    print(f"Enter room names one at a time, then enter a description. "
                          f"Enter \"Done\" when you have finished entering names.\n")
                    new_rooms = {}
                    while editing_rooms == True:
                        room_name = input("Enter Name: ").strip().title()
                        if room_name == "Done":
                            print("Changed Room List: ", end="")
                            for index, room in enumerate(new_rooms):
                                print(room, ":", new_rooms[room],)
                            finalize_nav = input("\nDo you want to re-write rooms for this preset? (Y/N): ").strip().upper()
                            if finalize_nav == "Y":
                                write_preset(current_preset_name, new_rooms, new_npc_list, new_npc_attributes, "room")
                            elif finalize_nav == "N":
                                print("\n...Redirecting...\n")
                            editing_rooms = False
                            print_preset_names()
                        else:
                            room_description = input(f"Enter {room_name} Description: ").strip().capitalize()
                            new_rooms[room_name] = room_description

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
                                write_preset(current_preset_name, new_rooms, new_npc_list, new_npc_attributes, "npc")
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
                    print_preset_names()



            else:
                input("\nFile name not recognized. Try again. (Enter)")

    def custom_presets():
        wipe()
        create_over = False
        global user_name
        while create_over == False:
            name_accepted = False
            print_preset_names()
            preset_nav_code = input(f"\nEnter \"C\" to create a new preset, enter \"E\" to edit, or enter anything else to return: ")
            if preset_nav_code.strip().upper() == "C":
                while name_accepted == False:
                    preset_name = input("\nEnter the name of your new preset file or enter \"R\" to return: ")
                    if preset_name.strip().upper() == "R":
                        name_accepted = True
                    elif os.path.exists(preset_name) or os.path.isfile(preset_name):
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