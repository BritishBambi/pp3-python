import time

# Item Dictionaries
baseball_bat = {
    "name": "Baseball Bat",
    "equipped": False
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
    start_game = input("Do you have what it takes to start your journey? yes/no:\n")
    if start_game == "yes":
        print("That's the spirit!\n")
        time.sleep(2)
        choice_1()
    elif start_game == "no":
        print("You do not have what it takes...\n")
        time.sleep(2)
        print("GAME OVER")
        time.sleep(2)
        play_again()

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
    equip_weapon = input("Do you want to bring a weapon with you? yes/no:\n")
    if equip_weapon == "yes":
        baseball_bat.update({"equipped": True})
        print(f"You have taken your trusty {bat} with you!")
        time.sleep(2)
        choice_2()
    elif equip_weapon == "no":
        print("You have decided to not bring a weapon..")
        time.sleep(2)
        choice_2()

def choice_2():
    print("Choice 2")  


def play_again():
    """
    Will allow the game to be ran again when and end condition is met"
    """
    play_again = input("Would you like to play again? yes/no:\n")
    if play_again == "yes":
        game_intro()
    elif play_again == "no":
        print("That's unfortunate, see you next time!")
        

game_intro()