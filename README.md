# Guess 'Em or Burst :

### A variant of hangman game
<br/>

## Video Demo :

[![video demo](https://img.youtube.com/vi/ud9_BmTl4sE/0.jpg)](https://www.youtube.com/watch?v=ud9_BmTl4sE)



## Description:

### Project Overview

Guess'Em or Burst is a little game implemented using pygame.

 It is a variation of the classic word-guessing game, Hangman. In this version, the game is themed around an amusement park, where instead of body parts being revealed, blue balloons burst when the player fails to guess correctly. The point was to add a  cute and entertaining twist to the traditional gameplay.

### Installation and Setup:

Before running the game, please ensure that you have the necessary dependencies installed. The requirements are specified in requirements.txt file.

**To set up the game, follow these steps:**

Create a virtual environment. If you, as me, prefer using virtualenv, run the following command:

> `virtualenv [virtual_environment_name].`

Install the dependencies by executing: 
> `pip install -r requirements.txt.`

Finally, run the game by executing the following command:
> `python3 project.py.`

### Usage:

When `project.py` is executed, pygame main loop starts displaying the main view, which presents two options:
Start and Exit.

Start: Selecting this option initiates the game by fetching a random word from the WonderWords API. The chosen word is displayed with all its letters replaced by underscores. The player can then type in letters using the keyboard. If the letter is included in the word, the corresponding underscore is replaced with the letter. Otherwise, if the letter is not present, one balloon will burst. The game continues until the player either runs out of balloons or correctly guesses the entire word.

Exit: Choosing this option ends the script and closes the window.

Additionally, at any moment during the game, the player can quit by clicking a red button with an 'X'."

### Project structure:

The project consists of several key components and modules:

> `project.py`: This file contains the main loop of pygame, which handles the input and output of the game, updating the view accordingly. It also includes other important functions such as:
    >>` load_image()`, responsible for loading the background and balloons.
    >> `draw_button()`,draws buttons with the given values received as parameters for position, size , etc.
    >> `draw_text_box()` , similar to previuos , but this draws texts box.

> `fetch_word`: This function is responsible for fetching a random word from the WonderWords API.

>`game()`: This function manages the game logic, determining if the player has guessed correctly and keeping track of the progress of the word and the number of tries.

>`play()`: This function returns an object with the necessary data to start playing.

>`main()`: This file includes various other functions to draw buttons and text boxes, ensuring a clean and organized structure.

In addition, there is a separate file named `constants.py`, which stores constant values to maintain clarity in main.py file.

For testing purposes, there is a file named `test-project.py` wich implements pytest and contains tests for all mentioned functions.

`Images` directory holds the static files required for the game, as background and balloon images.


### Technologies and Tools:

The project utilizes the following technologies and tools:

exceptiongroup==1.1.1
iniconfig==2.0.0
packaging==23.1
pluggy==1.2.0
pygame==2.4.0
pytest==7.4.0
tomli==2.0.1
wonderwords==2.2.0

These packages and libraries were used to support various aspects of the project's development, including exception handling (exceptiongroup), configuration file parsing (iniconfig), package management (packaging), game development (pygame), testing (pytest) and fetching random words from the WonderWords API (wonderwords)."

### Milestones and Development Process:

The development of this project consisted of several milestones and challenges:

**Initial Prompt Version**: The project started with a simple prompt-based version of the game, where the player interacted with the console. Although it was fun, I decided to challenge myself by using pygame, a powerful library for game development. This transition allowed for a more immersive and visually appealing experience.

**Learning Pygame**: Implementing pygame was a real challenge as I had no experience with the library. I relied on tutorials and the official documentation to grasp the basic concepts and functionalities. It was both exciting and demanding to make everything work together, especially since I had a basic understanding of object-oriented programming. Despite the learning curve, I managed to achieve the desired results within a relatively short timeframe.

**Object-Oriented Approach**: Going forward, I plan to enhance the project by adopting a more object-oriented approach. This will enable me to improve the code structure, organization, and reusability of components.

**Future Enhancements**: In the future, I aim to introduce new features to the game, such as different difficulty levels or integrating a database to keep track of player records. These additions will further enhance the gameplay experience and provide additional challenges and engagement for players.

Throughout the development process, I encountered various learning opportunities, and while there is always room for improvement, I am proud of what I have accomplished thus far. I am excited to continue refining and expanding the project in the future


### Attributions

The following images have been used in this project and require attribution to the respective authors:

- Image: Amusement park,used as background 

    <img width=150 src='images/1208.jpg'/>

  Source: [<a href="http://www.freepik.com">Designed by upklyak / Freepik</a>]

  Author: [upklyak]
  
  License:[License free-1208.txt]

- Image: [Blue balloons]

    <img width=150 src='images/balloon.gif'/>

  Source: [<a href= 'https://www.deviantart.com/dumplingkitten/art/New-Balloon-Gif-662705736'>Ballon gif</a>]

  Author: [dumplingkitten]
