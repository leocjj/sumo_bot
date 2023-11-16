# Python Sumo Bot - Using Pygame

This is a sumo bot game using Pygame. The game is played by two players. The objective of the game is to push the opponent out of the ring. The player who pushes the opponent out of the ring wins the round.

Each player should write a code to move their bots in the ring. The codes should be written in the files player1.py and player2.py using the function move_bot(...).


## Installation

### 1. Installing Python

If you already have Python installed on your computer, you can skip this step.

### 1.1 Windows

If you are using Windows, you can install Python from [here](https://www.python.org/downloads/), and make sure you select the option to add Python to the path during the installation.

You can also install Python using [miniconda](https://docs.conda.io/projects/miniconda/en/latest/miniconda-install.html) (Recommended). In this case, you will need to use the newly installed Anaconda Powershell Prompt instead of the Windows command prompt or Windows Powershell.

### 1.2 Linux or Mac
If you are using Linux or Mac, Python is already installed on your computer. [Miniconda](https://docs.conda.io/projects/miniconda/en/latest/miniconda-install.html) can be installed too (Recommended). In the next steps, you will need to use Terminal.

### 2. Creating a Python virtual environment (Optional)
Creating a virtual environment is optional but recommended. Open Anaconda Powershell Prompt (Windows) or Terminal (Linux and Mac) and type the following commands.

```bash
conda create -n sumo_bot python=3.10 -y
conda activate sumo_bot
```

### 3. Pygame installation

Once you have Python installed on your computer, install Pygame using pip. Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Pygame.

```bash
pip install pygame==2.5.2
git clone https://github.com/leocjj/sumo_bot.git
cd sumo_bot
```

## Usage
To run the game use the following command inside the sumo_bot directory:

```bash
python main.py
```

Each player should put its own code in the corresponding file: player1.py or player2.py.
The codes should be written in the function move_bot().

This function will receive each frame, the coordinates (x, y), and the actual (positive) rotation angle (rot) of its own bot
and the opponent bot (x_opp, y_opp, rot_opp).

The angles are zero in the horizontal axis to the left, positive if it goes counterclockwise from zero or
negative if it goes clockwise from zero (e.g. 270° and -90° are the same rotation angle).

At the end, it should return two values (a tuple of integers):
 - The first value is for the next movement: 1 to move forward, 0 to stop, and -1 to move backward.
 - The second value is for the next rotation: 1 to rotate counterclockwise, 0 to stop, and -1 to rotate clockwise.
```python
def move_bot(x: int, y: int, rot: int, x_opp: int, y_opp: int, rot_opp: int) -> tuple[int, int]:
    # Write your code here

    # Return the movement and rotation, for example: rotate counterclockwise all the time.
    return 0, 1
```

## Debugging
Change this variable in the file main.py to move the bots automatically, semi-automatically, or manually.

```python
# 0: Automatic mode for both bots. No keyboard inputs.
DEBUG_MODE = 0

# 1: Automatic mode for player 1 bot only. The player 2 can be moved with the keyboard.
DEBUG_MODE = 1

# 2: Automatic mode for player 2 bot only. The player 1 can be moved with the keyboard.
DEBUG_MODE = 2

# 3: Automatic mode for both player bots and both players can use the keyboard too.
DEBUG_MODE = 3

# 4: Manual mode for both player players with the keyboard.
DEBUG_MODE = 4
```

The players can use the following keys to move:
* Player 1: W (forward), A (rotate CCW), S (backward), D(rotate CW)
* Player 2: Up (forward), Left (rotate CCW), Down (backward), Right(rotate CW)

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
* Beta version

## To Do
* Add more features: obstacles, different ring shapes, etc.
* Add more comments and help.
* Add more documentation.
* Add more examples and tests.

## Change Log
* 2023-11-16: Beta version completed
