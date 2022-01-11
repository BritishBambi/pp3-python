import time


# Item Dictionaries
baseball_bat = {
    "name": "Baseball Bat",
    "equipped": False,
    "durability": "2"
}


# Global Variables
bat = baseball_bat.get("name")


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
                baseball_bat.update({"durability": "1"})
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
            print("Unfortunatly, you ran into a horde")
            time.sleep(2)
            print("You become overwhelmed and attacked by over 10 zombies")
            time.sleep(2)
            print("GAME OVER")
            play_again()
            break
        else:
            print("Invalid input, please type yes or no")
            continue


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
