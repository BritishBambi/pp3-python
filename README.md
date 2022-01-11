# Hunted

Hunted is a text adventure game. The player will be brought through a zombie survival story, where they must scavange for food to survive. Along the way they must use items and their intelegence to navigate safley through the dangers of the world they live in.

The game story is inspired by other zombie games that depend on the use of resources and weapons in order to survive. While younger players may not fit the target audience, older players may love the call back to orignal text games.

## How to Play

The game is mainly played via a simple Yes or No input from the user. More of the complexity to winning comes from the user's ability to use items and resources to reach the end. The decision weather or not to fight or retreat depending on their inventory.

The goal is to retrieve items from an abandonded store and return back to their home base. This gives the user a clear goal that stays in their head throughout the story.

When the game is first loaded the user will be presented with a short introduction to the world of the game. Then they will be asked weather or not they are ready to start the game. This will quickly give the user agency to start or not so they do not have to sit through a long screen each time. The user will be able to go down multiple branches through the game and can make the decision to take items and use them. However the items will have a durability so if they are used too often then they will eventually break and be unusable later in the game. This means the user has to make smart choices when given the option. By utilising these items and choices they will be able to win and make it back to survive.

## Features

## Testing

### Play Again

Whenever the user reaches and end condition the game will run the play_again function. This will present the user with a yes or no question as to weather or not they want to try again. If yes is typed the user is successfully brought back to the beginning by running the game_intro function. This loops the user back to the beginning of the game. We also make sure to include dictonary updates to make sure the play again does not intefere with the default values of the dictonary. Similarly when the user types no, the game will display a short message and the programn stops as expected. If any other input is detected then the programn will tell the user an invalid input was detected and the question will be asked again.

## Technologies

Python
Github
Gitpod
Python Time module

## Deployment

## Credits

Adding delay to code learnt from: https://realpython.com/python-sleep/

Using While loops to allow invalid inputs to return back to choice question from: https://stackoverflow.com/questions/12828771/how-to-go-back-to-first-if-statement-if-no-choices-are-valid

## Aknowledgements