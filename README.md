# Table of Contents

- [Table of Contents](#table-of-contents)
- [Project 3 - Python - ](#python-the-hangman-game)
- [UX](#ux)
    - [Strategy](#strategy)
    - [Scope](#scope)
    - [Structure](#structure)
    - [Skeleton](#skeleton)
    - [Surface](#surface)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Testing](#testing)
- [Deployment](#deployment)
- [Credits](#credits)


# Python The Hangman Game

This Python application responds to the users' input, allowing them to play the game of The Hangman with the computer.

( This is as a milestone project for the Python module of the Full Stack Web Development Course at Code Institute. )


## Demo

To access live demo, click <a href="https://the-hangman-game-project.herokuapp.com/" target="_blank"> here. </a>

# HOW TO PLAY

* From the main menu, the user can choose to play the game straight away, read the instructions or choose a difficulty level. When the game commences a word is chosen by the computer and hidden from the user. Depending on the difficulty level, the user will have either 3, 6 or 9 attempts to guess a letter or the whole word at once. During the game a graphic of gallows will be displayed and with each wrong guess elements will be added to it until the whole image will emerge. Alternatively, if the user guesses right the game ends with a display of a 'Victory' image. Either way, when the game ends, the user will be given an option to restart the game or not. If he chooses not to, he/she will be returned to the main menu.
Throughout the game the user is shown placeholders which represent how many letters are contained within the word and with each guessed letter, the right guess takes the place of the placeholders.

# UX

## Strategy

User's expectations:
* The application allows the user to play a guessing game called Tha Hangman with computer. The user has to guess a word which is hidden, given a specified amount of tries. 

Target Users:
* Anyone who wishes to play the game of guessing a secret, hidden word in their free time and is familiar with the use of terminal.

User Stories:
* As a visitor to the application, I want to play The Hangman game.

## Scope

### Content Requirements
* Information presented in the terminal guides the user, enabling him/her to play the game and choose relevant options and play the game.

### Functional Requirements
* User's input is processed and results are presented in the terminal.

## Structure

### Interaction Design

* Clear presentation of options available to the user in the main menu and menu for choosing difficulty
* The terminal asks the user for input once the game starts and throughout it reacts to users input with relevant choices.

### Information Architecture

* All content and information is presented in the terminal by text and graphics.
* The program informs the user about the results of interaction with relevant information presented in the terminal.

## Skeleton

### Navigation Design

* The user is guided by relevant requests and information through the process of playing the game.

### Interface design

* The game is contained inside the mock terminal provided by Code Institute.

### Wireframes - Flowchart

Flowchart for the project can be found <a href="https://github.com/Cezary-Nakielski/Project-Three-The-Hangman/blob/main/assets/flowchart.png" target="_blank"> here. </a>

##  Surface

* Terminal created and supplied by Code Institute
* Colours making the information more readable and pleasant - Also indicating intuitive association with the state of the game/result of input
* The intro_graphic is intentionally visible only half way. The user has to scroll up to see the gallows.

## Features

### Existing Features
 
* Random words generation
- The word is chosen by the computer and hidden from the user
* Feedback on the progress of the game, effects of the users input on the program - correct/incorrect input, guess/missed guess, win/defeat - Validation and checking for errors
- Text informs the user about choices which are available
- Graphical diplay of gallows shows the user progress of the game
- 'Victory' and 'Defeat' graphics inform the user about the end result of the game 
* Option to see game instructions
* Option to choose difficulty

### Features Left to Implement

* Timer - The user would have limited time to guess. The amount of time would depend on the difficulty level.
* Scoreboard
* More words in the random_words file, although "Veteran" difficulty could be too difficult if to many words would be added.

## Technologies Used

- [Python] - coding language used in the development of the project
- https://app.diagrams.net/ - to make a Flowchart
- https://patorjk.com/software/taag - to make graphics for the 'progress', 'intro_title', 'victory' and 'defeat' functions

## Testing

Manual Testing Implemented:

- During development (using https://replit.com and https://pythontutor.com) and after deployment tests were made to make sure that the user receives relevant feedback on the input entered. This includes correct input, where the game would proceed, the game would end with win or defeat, as well as incorrect character input, repeated input or no input. (Due to blocks of code being tested on external platform - https://replit.com - and put back into Gitpod erroneously or in wrong place several times, the code during development did not work properly in Gitpod at early stages of the project. Corrections were made along the way.)

- Python Linter (http://pep8online.com/) was used to validate code and make sure it's error-free.

## Bugs

No known bugs left to correct.

At the beginning of development I used https://replit.com and https://pythontutor.com to write and test blocks of code, but I stopped due to many errors which I encountered after testing the deployed project from the mock terminal. From that point on I started testing the code throughout direct input to mock terminal.

On multiple occasions I had to remove whitespaces after adding graphics, correct typos which were causing errors and refactor the code where string literals where needed.


## Deployment

* Clone or fork this repository
* Create account with Heroku and crete there a new app
* Add a Config Var with key 'PORT' and value '8000' in Heroku's Settings
* Add buildbacks first for Python and then for NodeJS
* Link the app to repository:
- either manually and click to Deploy Branch or
- enable automatic deploys and follow given instructions

## Credits

### Content

- The Graphics for displaying the game Title, Win and Defeat images were generated using (https://patorjk.com/software/taag)


### Acknowledgements

- I received inspiration and information necessary for this project from lessons and material provided by Code Institute, video and text tutourials found online as well as my mentor to whom I am very grateful for his understanding and expertise.

- Helpful sources of information outside of Code Institute used in the creation of the project:
    - (https://inventwithpython.com/invent4thed/chapter8.html)
    - (https://www.youtube.com/watch?v=cJJTnI22IF8&ab_channel=KylieYing)
    - (https://www.youtube.com/watch?v=5x6iAKdJB6U&ab_channel=NeuralNine)
    - (https://www.youtube.com/watch?v=m4nEnsavl6w&ab_channel=Kite)
    - (https://www.youtube.com/watch?v=JNXmCOumNw0&ab_channel=CBTNuggets)

- I found Stackoverflow (https://stackoverflow.com/) the best place to find answers when something wasn't working as I expected it to.

- Random words generator:
    - (https://randomwordgenerator.com/)

- Flowchart creation tool:
    - (https://app.diagrams.net/)

- Validator services:
    -[Python] (http://pep8online.com/)

- Thanks to Code Institute for the mock terminal and template provided!

* This website was made for educational purposes