# Snake Water Gun Game

A simple **console-based Python game** where you play Snake, Water, and Gun against the computer. This project was developed as a **university assignment** to demonstrate basic Python programming concepts including functions, dictionaries, user input handling, and game logic.

---

## Table of Contents

- [About the Game](#about-the-game)
- [Game Rules](#game-rules)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Installation](#installation)
- [How to Run](#how-to-run)
- [How to Play](#how-to-play)
- [Sample Output](#sample-output)
- [Program Logic](#program-logic)
- [Future Improvements](#future-improvements)
- [Author](#author)
- [License](#license)

---

## About the Game

**Snake Water Gun** is a variation of the classic Rock-Paper-Scissors game. Instead of rock, paper, and scissors, players choose between **Snake**, **Water**, and **Gun**. The player competes against the computer in multiple rounds, and scores are tracked throughout the session.

This game is played entirely in the terminal — no graphical interface is required.

---

## Game Rules

Each choice beats exactly one other choice:

| Your Choice | Beats   | Explanation              |
|-------------|---------|--------------------------|
| Snake (s)   | Water   | Snake drinks the water   |
| Water (w)   | Gun     | Water rusts the gun      |
| Gun (g)     | Snake   | Gun kills the snake      |

- If both players choose the same option, the round is a **draw**.
- The game continues until you choose not to play again.

---

## Features

- Interactive command-line gameplay
- Random computer opponent
- Input validation with helpful error messages
- Round-by-round result display
- Live scoreboard (wins, losses, draws)
- Play-again option after each round
- Clean, modular, and well-documented code

---

## Technologies Used

| Technology | Purpose                          |
|------------|----------------------------------|
| Python 3   | Core programming language        |
| `random`   | Computer's random choice         |
| `typing`   | Type hints for better readability |

No external libraries or frameworks are required.

---

## Project Structure

```
Snake-water-gun-game/
│
├── main.py              # Main game logic and entry point
├── requirements.txt     # Project dependencies (none required)
├── .gitignore           # Git ignore rules for Python projects
└── README.md            # Project documentation
```

---

## Requirements

- **Python 3.8 or higher**
- A terminal / command prompt

Verify your Python installation:

```bash
python --version
```

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/lintaash17/snake-water-gun-game.git
cd snake-water-gun-game
```

### 2. (Optional) Create a virtual environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

### 3. Install dependencies

This project has no external dependencies. The `requirements.txt` file is included for completeness.

```bash
pip install -r requirements.txt
```

---

## How to Run

From the project directory, execute:

```bash
python main.py
```

---

## How to Play

1. Run the program using the command above.
2. Read the rules displayed at the start.
3. Enter your choice when prompted:
   - `s` → Snake
   - `w` → Water
   - `g` → Gun
   - `q` → Quit
4. View the computer's choice and the round result.
5. Check the updated scoreboard.
6. Type `y` to play another round or `n` to exit.

---

## Sample Output

```
=== Snake • Water • Gun ===

Rules:
  • Snake drinks Water  → Snake wins
  • Water rusts Gun     → Water wins
  • Gun kills Snake     → Gun wins

Controls:
  [s] Snake   [w] Water   [g] Gun   [q] Quit

Your choice: s

----------------------------
You       : Snake
Computer  : Water
----------------------------
Result    : You Win!

Scoreboard → You: 1 | Computer: 0 | Draws: 0

Play again? (y/n): n

Thanks for playing! Final score:

Scoreboard → You: 1 | Computer: 0 | Draws: 0
```

---

## Program Logic

The game follows this flow:

```
Start
  │
  ▼
Display rules and controls
  │
  ▼
Get player choice (validate input)
  │
  ├── Invalid → show error, ask again
  ├── Quit (q) → show final score and exit
  │
  ▼
Generate random computer choice
  │
  ▼
Compare choices using WINNING_MOVES dictionary
  │
  ▼
Display result and update scoreboard
  │
  ▼
Ask to play again
  │
  ├── Yes → repeat
  └── No  → show final score and exit
```

### Key Functions

| Function               | Description                              |
|------------------------|------------------------------------------|
| `display_rules()`      | Shows game rules and keyboard controls   |
| `get_player_choice()`  | Reads and validates player input         |
| `get_computer_choice()`| Picks a random move for the computer     |
| `determine_winner()`   | Compares choices and returns the outcome |
| `play_round()`         | Runs a single round of gameplay          |
| `main()`               | Controls the overall game loop           |

---

## Future Improvements

Possible enhancements for future versions:

- [ ] GUI using Tkinter or Pygame
- [ ] Two-player local mode
- [ ] Save high scores to a file
- [ ] Add sound effects
- [ ] Unit tests for game logic

---

## Author

**Linta Ashafq**  

---

## License

This project is created for educational purposes as part of a university assignment.

You are free to use and modify this code for learning. If you share it, please give appropriate credit.
