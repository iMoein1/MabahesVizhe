import random

MAX_ATTEMPTS = 10

DIFFICULTIES = {
    "1": ("Easy", 50),
    "2": ("Medium", 100),
    "3": ("Hard", 500),
}


def choose_difficulty():
    print("\nChoose a difficulty:")
    for key, (name, high) in DIFFICULTIES.items():
        print(f"  {key}. {name} (1-{high})")
    while True:
        choice = input("Your choice: ").strip()
        if choice in DIFFICULTIES:
            return DIFFICULTIES[choice]
        print("Please enter 1, 2, or 3.")


def ask_guess(high, previous):
    """Keep asking until the input is a valid, new number in range.
    Invalid input never costs an attempt."""
    while True:
        raw = input("Your guess: ").strip()
        try:
            guess = int(raw)
        except ValueError:
            print("Please enter a whole number.")
            continue
        if not 1 <= guess <= high:
            print(f"Out of range. Enter a number between 1 and {high}.")
            continue
        if guess in previous:
            print("You already tried that number.")
            continue
        return guess


def play_round():
    """Play one round. Returns True on a win, False on a loss."""
    name, high = choose_difficulty()
    secret = random.randint(1, high)
    low_bound, high_bound = 1, high  # narrows as the player gets hints
    guesses = []

    print(f"\n{name} mode: I'm thinking of a number between 1 and {high}.")
    print(f"You have {MAX_ATTEMPTS} attempts.\n")

    for attempt in range(1, MAX_ATTEMPTS + 1):
        remaining = MAX_ATTEMPTS - attempt + 1
        print(f"Attempt {attempt}/{MAX_ATTEMPTS} ({remaining} left) | "
              f"The number is between {low_bound} and {high_bound}")
        guess = ask_guess(high, guesses)
        guesses.append(guess)

        if guess == secret:
            print(f"\nYou win! You got it in {attempt} attempt(s).")
            print(f"Your guesses: {guesses}")
            return True

        if guess < secret:
            low_bound = max(low_bound, guess + 1)
            print("Too low!\n")
        else:
            high_bound = min(high_bound, guess - 1)
            print("Too high!\n")

    print(f"You lose! The number was {secret}.")
    print(f"Your guesses: {guesses}")
    return False


def ask_play_again():
    while True:
        answer = input("\nPlay again? (y/n): ").strip().lower()
        if answer in ("y", "yes"):
            return True
        if answer in ("n", "no"):
            return False
        print("Please answer y or n.")


def main():
    wins = losses = 0
    print("=== Number Guessing Game ===")
    try:
        while True:
            if play_round():
                wins += 1
            else:
                losses += 1
            print(f"Score -> Wins: {wins} | Losses: {losses}")
            if not ask_play_again():
                break
    except (KeyboardInterrupt, EOFError):
        print()  # clean line after Ctrl+C / Ctrl+D

    print(f"\nFinal score -> Wins: {wins} | Losses: {losses}. Thanks for playing!")


if __name__ == "__main__":
    main()