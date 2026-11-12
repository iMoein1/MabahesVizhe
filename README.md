# Number Guessing Game

A command-line game written in Python. The computer picks a random number, and you have **10 attempts** to guess it. Guess it within 10 attempts and you win; fail and you lose.

## Requirements

- Python 3.6 or newer
- No third-party packages (standard library only)

Check your version:

```bash
python3 --version
```

## Running the game

Save `guess_game.py` anywhere, open a terminal in that folder, and run:

```bash
python3 guess_game.py
```

On Windows, you may need to use `python` or `py` instead:

```bash
python guess_game.py
```

## How to play

1. **Choose a difficulty** by typing `1`, `2`, or `3`.
2. **Guess the number.** Type a whole number and press Enter.
3. **Read the hint.** The game tells you whether your guess was too low or too high, and shows the range the number must now be in.
4. **Keep going** until you guess correctly (win) or use all 10 attempts (lose).
5. **Play again** if you like. Your wins and losses are tallied across rounds.

### Difficulty levels

| Option | Mode   | Number range | Attempts |
|--------|--------|--------------|----------|
| 1      | Easy   | 1 to 50      | 10       |
| 2      | Medium | 1 to 100     | 10       |
| 3      | Hard   | 1 to 500     | 10       |

### Rules

- You win if you guess the number in 10 attempts or fewer.
- You lose if you haven't guessed it after 10 attempts. The secret number is then revealed.
- Invalid input **does not use up an attempt**:
  - Anything that isn't a whole number (e.g. `abc`, `3.5`)
  - A number outside the current difficulty's range
  - A number you have already guessed

## Example session

```
=== Number Guessing Game ===

Choose a difficulty:
  1. Easy (1-50)
  2. Medium (1-100)
  3. Hard (1-500)
Your choice: 2

Medium mode: I'm thinking of a number between 1 and 100.
You have 10 attempts.

Attempt 1/10 (10 left) | The number is between 1 and 100
Your guess: 50
Too high!

Attempt 2/10 (9 left) | The number is between 1 and 49
Your guess: 25
Too low!

Attempt 3/10 (8 left) | The number is between 26 and 49
Your guess: 37

You win! You got it in 3 attempt(s).
Your guesses: [50, 25, 37]
Score -> Wins: 1 | Losses: 0

Play again? (y/n): n

Final score -> Wins: 1 | Losses: 0. Thanks for playing!
```

## Quitting

Press `Ctrl+C` (or `Ctrl+D` on macOS/Linux) at any time to exit. The game prints your final score and closes cleanly.

## Customizing

Open `guess_game.py` and edit the constants near the top:

```python
MAX_ATTEMPTS = 10

DIFFICULTIES = {
    "1": ("Easy", 50),
    "2": ("Medium", 100),
    "3": ("Hard", 500),
}
```

- Change `MAX_ATTEMPTS` to give players more or fewer tries.
- Edit, add, or remove entries in `DIFFICULTIES`. Each entry maps a menu key to a `(name, highest_number)` pair, and the menu updates automatically. If you add a fourth option, the prompt message in `choose_difficulty()` ("Please enter 1, 2, or 3.") should be updated to match.

## Project structure

```
.
├── guess_game.py   # the game
└── README.md       # this file
```