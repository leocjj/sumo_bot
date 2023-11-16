# PYTHON SUMO BOT - Using Pygame

This is a sumo bot game using Pygame. The game is played by two players. The objective of the game is to push the opponent out of the ring. The player who pushes the opponent out of the ring wins the round.

Each player should write a code to move its bot in the ring. The codes should be written in the files player1.py and player2.py using the function move_bot(...).


## 1. Python installation

If you already have Python installed in your computer, you can skip this step.

### 1.1 Windows

If you are using Windows, you can install Python from [here](https://www.python.org/downloads/) and make sure you select the option to add python to the path during the installation.

You can also install python using [miniconda](https://docs.conda.io/projects/miniconda/en/latest/miniconda-install.html) (Recommended). In this case you will need to use the new installed Anaconda Powershell Prompt instead of the Windows command prompt or Windows Powershell.

### 1.2 Linux and Mac
If you are using Linux or Mac, Python is already installed in your computer. [Miniconda](https://docs.conda.io/projects/miniconda/en/latest/miniconda-install.html) can be installed too (Recommended). In the next steps, you will need to use Terminal.

## 2. Creating a Python virtual environment (Optional)
Creating a virtual environment is optional but recommended. Open Anaconda Powershell Prompt (Windows) or Terminal (Linux and Mac) and type the following commands.

```bash
conda create -n sumo_bot python=3.10
conda activate sumo_bot
```

## 3. Pygame installation

Asumming you have Python installed in your computer, install Pygame using pip. Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Pygame.

```bash
pip install pygame
git clone https://github.com/leocjj/sumo_bot.git
cd sumo_bot
```

## Usage

Each player should put its code in the corresponding file: player1.py or player2.py. The codes should be written in the function move_bot() and should return two values:
 - First value with the movement:1 forward, 0 to stop, and -1 for backward.
 - Second value with the rotation: 1 to rotate counterclockwise, 0 to stop, and -1 to rotate clockwise.
```python
def move_bot(x: int, y: int, rot: int, x_opp: int, y_opp: int, rot_opp: int) -> tuple[int, int]:
    # Write your code here

    # Return the movement and rotation, for example: rotate counterclockwise all the time.
    return 0, 1
```
Then, run the game using the following command:

```python
python main.py
```

## Debugging
Change this variable in the file main.py to move the bots automatically, semi-automatically, or manually.

```python
# 0: Automatic mode for both bots. No keyboard inputs.
DEBUG_MODE = 0

# 1: Automatic mode for player 1 only. Player 2 can be moved with the keyboard.
DEBUG_MODE = 1

# 2: Automatic mode for player 2 only. Player 1 can be moved with the keyboard.
DEBUG_MODE = 2

# 3: Automatic mode for both player players and also both can be moved with the keyboard.
DEBUG_MODE = 3

# 4: Manual mode for both player players with the keyboard.
DEBUG_MODE = 4

```


The players can use the keys: W, A, S, D (player 1) and Up, Down, Left, Right (player 2).


## Game Rules
* The game is played by two players.
* The objective of the game is to push the opponent out of the ring.
* The player who pushes the opponent out of the ring wins the round.
* The player who wins the most rounds wins the game.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Authors
* **Leo CJJ** - *Initial work* - [leocjj](https://github.com/leocjj)

## License
[GPL-3.0](https://www.gnu.org/licenses/gpl-3.0.en.html)

## Acknowledgments
AI that helped me to write the code, comments, and documentation:
* [Copilot](https://copilot.github.com/)

## References
Game framework:
* [Pygame](https://www.pygame.org/docs/)

## Contact
[leocjj](https://github.com/leocjj)

## Project Status
* Alpha version Completed
* Beta version In Progress

## To Do
* Add more features: obstacles, different ring shapes, etc.
* Add more comments and help.
* Add more documentation.
* Add more examples and tests.

## Change Log
* 2023-11-16: Alpha version completed
