import time

# Item Dictionaries
baseball_bat = {
    "name": "Baseball Bat",
    "equipped": False
}

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
    
    print("It has been 5 years since they took over the earth..")
    time.sleep(2)
    print("You have been surviving by any means necessary")
    time.sleep(2)
    print("To survive you need food, and must find some before you starve")
    time.sleep(2)
    start_game = input("Do you have what it takes to start your journey? yes/no:\n")
    if start_game == "yes":
        print("That's the spirit!")
        time.sleep(2)
        choice_1()
    elif start_game =="no":
        print("You do not have what it takes...")
        time.sleep(2)
        print("GAME OVER")
        time.sleep(2)
        play_again()


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