import time
from colorama import Fore, Style


# Item Dictionaries
baseball_bat = {
    "name": "Baseball Bat",
    "equipped": False,
    "durability": 3
}

ghillie_suit = {
    "name": "Ghillie Suit",
    "equipped:": False
}


# Global Variables
bat = baseball_bat.get("name")
ghillie = ghillie_suit.get("name")


def game_intro():
    """
    Will display the game introduction and welcome screen to the user when ran.
    """
    print("Welcome to Scavenge")
    time.sleep(2)
    print("This text based adventure game will test your skills...")
    time.sleep(2)
    print("It's time to face the zombie horde!\n")
    time.sleep(2)
    game_start()


def game_start():
    """
    Presents the user with a small story introduction
    and then asks them if they want to play via
    a story question.
    """
    print("It has been 5 years since they took over the earth..")
    time.sleep(2)
    print("You have been surviving by any means necessary")
    time.sleep(2)
    print("To survive you need food, and must find some before you starve")
    time.sleep(2)
    while True:
        start_game = input("Do you have what it takes to start? yes/no:\n")
        start_game = start_game.lower()
        if start_game == "yes":
            print("That's the spirit!\n")
            time.sleep(2)
            ghillie_suit.update({"equipped": False})
            choice_1()
            break
        elif start_game == "no":
            print("You do not have what it takes...\n")
            time.sleep(2)
            print(Fore.RED + "GAME OVER")
            print(Style.RESET_ALL)
            play_again()
            break
        else:
            print("Invalid input, please type yes or no")
            time.sleep(1)
            continue


def choice_1():
    """
    Presents the user with the first choice of the game.
    If the user brings the bat it will update the dictonary
    to refelct equipped as True. This will be used to influence
    choices later.
    """

    print("After a survey of the area, you found an abandoned shop nearby..")
    time.sleep(2)
    print("This may be a good place to search, or dangerous..")
    time.sleep(2)
    while True:
        equip_weapon = input("Do you want to bring a weapon? yes/no:\n")
        equip_weapon = equip_weapon.lower()
        if equip_weapon == "yes":
            baseball_bat.update({"equipped": True})
            baseball_bat.update({"durability": 3})
            print(f"You have taken your trusty {bat} with you!\n")
            time.sleep(2)
            choice_2()
            break
        elif equip_weapon == "no":
            baseball_bat.update({"equipped": False})
            print("You have decided to not bring a weapon..\n")
            time.sleep(2)
            choice_2()
            break
        else:
            print("Invalid input, please type yes or no")
            time.sleep(1)
            continue


def choice_2():
    """
    The first choice where options will be taken into account
    if certain conditions are reached then the user can reach
    choice 3 or branch 1 from here. This is done using if
    statements to take the users input and give them the
    corrosponding route.
    """
    print("On the way to the shop, you encounter a lone zombie..")
    time.sleep(2)
    print("It has yellow eyes and a decaying body..")
    time.sleep(2)
    print("Most importantly, it stands in your way..")
    time.sleep(2)
    while True:
        attack = input("Do you want to attack the zombie? yes/no:\n")
        attack = attack.lower()
        if attack == "yes":
            print("You decide to attack the zombie!")
            time.sleep(2)
            if baseball_bat.get("equipped") is True:
                print("You easily knock the zombie head clean off!")
                time.sleep(2)
                print(f"However the {bat} is looking weaker..")
                time.sleep(2)
                baseball_bat["durability"] -= 1
                print("Defeating the zombie has cleared a path to the shop\n")
                time.sleep(2)
                choice_3()
                break
            elif baseball_bat.get("equipped") is False:
                print("You try to attack with your fists!")
                time.sleep(2)
                print("This was not the best idea...")
                time.sleep(2)
                print("The Zombie overpowers you easily as you become dinner")
                time.sleep(2)
                print(Fore.RED + "GAME OVER")
                print(Style.RESET_ALL)
                play_again()
                break
        elif attack == "no":
            print("You try to find another way around\n")
            time.sleep(2)
            branch_1()
            break
        else:
            print("Invalid input, please type yes or no")
            time.sleep(1)
            continue


def branch_1():
    """
    The alternative route for the player reached only by
    avoiding the zombie in choice 2. Allows more routes
    for the player and can give the player equipment
    depending on their input.
    """
    print("You find some neighbouring buildings that offer a new route.")
    time.sleep(2)
    print("In the building you find a few ways out to the shop")
    time.sleep(2)
    print("You see a window to the street...")
    time.sleep(2)
    print("...A corridor with growling coming from it..")
    time.sleep(2)
    print("...and a living room with some cabinets")
    while True:
        building = input("Which way will you go? window/room/corridor?\n")
        building = building.lower()
        if building == "window":
            print("You go through the window and towards the shop\n")
            time.sleep(2)
            choice_3()
            break
        elif building == "corridor":
            print("You move towards the growling..\n")
            time.sleep(2)
            print("As expected you are jumped by multiple zombies.")
            time.sleep(2)
            print("You are overwhelmed and eaten alive!")
            time.sleep(2)
            print(Fore.RED + "GAME OVER")
            print(Style.RESET_ALL)
            play_again()
            break
        elif building == "room":
            print("You check the room..\n")
            time.sleep(2)
            print(f"In the room you find a {ghillie} for sneaking around!")
            time.sleep(2)
            print("This will make it easier to stealth")
            ghillie_suit.update({"equipped": True})
            time.sleep(2)
            print("Unfortunatly a zombie followed you in to the room!")
            if baseball_bat.get("equipped") is True:
                time.sleep(2)
                print(f"Since you are carrying a {bat} and {ghillie}..")
                time.sleep(2)
                print("..you are Over-encumbered and zombie overpowers you")
                time.sleep(2)
                print(Fore.RED + "GAME OVER")
                print(Style.RESET_ALL)
                play_again()
            elif baseball_bat.get("equipped") is False:
                time.sleep(2)
                print("With no weapon to slow you down you run for it")
                time.sleep(2)
            print("You then escape using a fire exit through the room\n")
            time.sleep(2)
            choice_3()
            break
        else:
            print("Invalid input, please type window/room/corridor")
            time.sleep(1)
            continue


def choice_3():
    """
    The final choice which will evaluate and check against all the
    equipment the user has taken so far to determine if they can
    reach the end of not. Depending on weather the user branched
    or not they will be able to only succeed on certain inputs.
    """
    print("You move through the streets, being careful as you do.")
    time.sleep(2)
    print("You find the shop however, 2 zombies wonder outside")
    time.sleep(2)
    while True:
        shop_aproach = input("How do you approach? stealth/attack/run\n")
        shop_aproach = shop_aproach.lower()
        if shop_aproach == "stealth":
            print("You opt for the quiet approach..")
            time.sleep(2)
            print("This is a smart idea.")
            time.sleep(2)
            if ghillie_suit.get("equipped") is True:
                print(f"Using the {ghillie} you sneak by both zombies!")
                time.sleep(2)
                shop()
                break
            elif ghillie_suit.get("equipped") is False:
                print("You are able to sneak by one of the zombies.")
                time.sleep(2)
                print("However, one of them spots you as you reach the door..")
                time.sleep(2)
                print("He attacks you!")
                if baseball_bat.get("equipped") is True:
                    print(f"Luckily, you use the {bat} to defend yourself")
                    time.sleep(2)
                    baseball_bat["durability"] -= 1
                    shop()
                    break
                elif baseball_bat.get("equipped") is False:
                    print("You do not have a weapon to defend yourself!")
                    time.sleep(2)
                    print("The zombie overpowers you and eats you")
                    time.sleep(2)
                    print(Fore.RED + "GAME OVER")
                    print(Style.RESET_ALL)
                    play_again()
                    break
        elif shop_aproach == "run":
            print("You run away from the shop")
            time.sleep(2)
            print("With no food to survive, you starve to death in days.")
            time.sleep(2)
            print(Fore.RED + "GAME OVER")
            print(Style.RESET_ALL)
            play_again()
            break
        elif shop_aproach == "attack":
            time.sleep(2)
            print("This is a risky move, I hope you are prepared!")
            time.sleep(2)
            if baseball_bat.get("equipped") is True:
                print(f"With the {bat} at the ready you make an attack!")
                time.sleep(2)
                print("You grunt loudly as you bash both the zombies in!")
                time.sleep(2)
                print("You have succesfully taken down the zombies!")
                baseball_bat["durability"] -= 2
                time.sleep(2)
                shop()
                break
            elif baseball_bat.get("equipped") is False:
                print("You try to attack with your fists!")
                time.sleep(2)
                print("This was not the best idea...")
                time.sleep(2)
                print("The Zombie overpowers you easily as you become dinner")
                time.sleep(2)
                print(Fore.RED + "GAME OVER")
                print(Style.RESET_ALL)
                play_again()
                break
        else:
            print("Invalid input, please type stealth/attack/run")
            time.sleep(1)
            continue


def shop():
    """
    The final section of the game, certain endings will be achieved
    depending on the users equipment. This function will check weather the
    items are equipped or not and then for the bat check the durability to
    give another ending. A win state will then be reached.
    """
    print("You have made it to the shop!\n")
    time.sleep(2)
    print("By using your wits or your strength you reached the end!")
    time.sleep(2)
    print("You find multiple tins of beans to last you for a while.")
    time.sleep(2)
    if baseball_bat.get("equipped") is True:
        print("Since you have cleared out the way you can make it back safe.")
        time.sleep(2)
        if baseball_bat.get("durability") == 0:
            print(f"That trusty {bat} got you all this way")
            time.sleep(2)
            print("What a shame it has been destroyed.")
            time.sleep(2)
        elif baseball_bat.get("durability") > 0:
            print(f"You were able to keep your trusty {bat} intact.")
            time.sleep(2)
            print("That'll be useful for the future.")
            time.sleep(2)
        print("You are able to stroll back home in safety!\n")
        time.sleep(2)
        print(Fore.GREEN + "You win!!! Enjoy the beans!")
        print(Style.RESET_ALL)
        time.sleep(2)
        play_again()
    if baseball_bat.get("equipped") is False:
        print(f"Using your {ghillie} you are able to sneak back home!\n")
        time.sleep(2)
        print(Fore.GREEN + "You win!!! Enjoy the beans!")
        print(Style.RESET_ALL)
        time.sleep(2)
        play_again()


def play_again():
    """
    Will allow the game to be ran again when and end condition is met"
    """
    while True:
        try:
            time.sleep(1)
            p_again = int(input("Would you like to play again? 1.Yes/2.No:\n"))
        except ValueError:
            print("Please type 1 or 2.")
        else:
            if p_again == 1:
                ghillie_suit.update({"equipped": False})
                time.sleep(1)
                choice_1()
                break
            elif p_again == 2:
                time.sleep(1)
                print("That's unfortunate, see you next time!")
                break
            else:
                print("Please type only 1 or 2.")
                continue


game_intro()
