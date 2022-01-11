import time

def game_intro():
    """
    Will display the game introduction and welcome screen to the user when ran.
    """
    print("Welcome to Hunted")
    time.sleep(2)
    print("This text based adventure game will test your skills...")
    time.sleep(2)
    print("Are you ready to face the zombie horde?")
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