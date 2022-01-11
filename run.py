import time


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
    print("Welcome to Hunted")
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
        if start_game == "yes":
            print("That's the spirit!\n")
            time.sleep(2)
            choice_1()
            break
        elif start_game == "no":
            print("You do not have what it takes...\n")
            time.sleep(2)
            print("GAME OVER")
            time.sleep(2)
            play_again()
            break
        else:
            print("Invalid input, please type yes or no")
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
        if equip_weapon == "yes":
            baseball_bat.update({"equipped": True})
            baseball_bat.update({"durability": 3})
            print(f"You have taken your trusty {bat} with you!")
            time.sleep(2)
            choice_2()
            break
        elif equip_weapon == "no":
            baseball_bat.update({"equipped": False})
            print("You have decided to not bring a weapon..")
            time.sleep(2)
            choice_2()
            break
        else:
            print("Invalid input, please type yes or no")
            continue


def choice_2():
    print("On the way to the shop, you encounter a lone zombie..")
    time.sleep(2)
    print("It has yellow eyes and a decaying body..")
    time.sleep(2)
    print("Most importantly, it stands in your way..")
    time.sleep(2)
    while True:
        attack = input("Do you want to attack the zombie? yes/no:\n")
        if attack == "yes":
            print("You decide to attack the zombie!")
            time.sleep(2)
            if baseball_bat.get("equipped") is True:
                print("You easily knock the zombie head clean off!")
                time.sleep(2)
                print(f"However the {bat} is looking weaker..")
                baseball_bat.update({"durability": 2})
                print("Defeating the zombie has cleared a path to the shop")
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
                print("GAME OVER")
                play_again()
                break
        elif attack == "no":
            print("You try to find another way around")
            time.sleep(2)
            branch_1()
            break
        else:
            print("Invalid input, please type yes or no")
            continue


def branch_1():
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
        if building == "window":
            print("You go through the window and towards the shop\n")
            choice_3()
            break
        elif building == "corridor":
            print("You move towards the growling..\n")
            time.sleep(2)
            print("As expected you are jumped by multiple zombies.")
            time.sleep(2)
            print("You are overwhelmed and eaten alive!")
            time.sleep(2)
            print("GAME OVER")
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
                print("GAME OVER")
                play_again()
            elif baseball_bat.get("equipped") is False:
                print("With no weapon to slow you down you run for it")
                time.sleep(2)
            print("You then escape using a fire exit through the room")
            choice_3()
            break
        else:
            print("Invalid input, please type yes or no")
            continue


def choice_3():
    print("You move through the streets, being careful as you do.\n")
    time.sleep(2)
    print("You find the shop however, 2 zombies wonder outside")
    time.sleep(2)
    while True:
        shop_aproach = input("How do you approach? stealth/attack/run\n")
        if shop_aproach == "stealth":
            print("You opt for the quiet approach..")
            time.sleep(2)
            print("This is a smart idea.")
            time.sleep(2)
            if ghillie_suit.get("equipped") is True:
                print(f"Using the {ghillie} you sneak by both zombies!")
                break
            elif ghillie_suit.get("equipped") is False:
                print("You are able to sneak by one of the zombies.")
                time.sleep(2)
                print("However, one of them spots you as you reach the door..")
                time.sleep(2)
                print("He attacks you!")
                if baseball_bat.get("equipped") is True:
                    print(f"Luckily, you use the {bat} to defend yourself")
                    baseball_bat.update({"durability": 1})
                    break
                elif baseball_bat.get("equipped") is False:
                    print("You do not have a weapon to defend yourself!")
                    time.sleep(2)
                    print("The zombie overpowers you and eats you")
                    time.sleep(2)
                    print("GAME OVER")
                    play_again()
                    break
        elif shop_aproach == "run":
            print("You run away from the shop")
            time.sleep(2)
            print("With no food to survive, you starve to death in days.")
            time.sleep(2)
            print("GAME OVER")
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
                time.sleep(2)
                print(f"Your trusty {bat} has broken but got you this far.")
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
                print("GAME OVER")
                play_again()
                break
        else:
            print("Invalid input, please type yes or no")
            continue


def shop():
    print("You have made it to the shop!")


def play_again():
    """
    Will allow the game to be ran again when and end condition is met"
    """
    while True:
        user_play_again = input("Would you like to play again? yes/no:\n")
        if user_play_again == "yes":
            game_intro()
            break
        elif user_play_again == "no":
            print("That's unfortunate, see you next time!")
            break
        else:
            print("Invalid input, please type yes or no")
            continue


game_intro()
