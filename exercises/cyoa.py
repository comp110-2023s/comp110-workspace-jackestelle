"""EX06 - Create your own adventure."""
__author__ = "730558551"
import random
points: int = 0  # Define the global variable points outside of main()
player: str = ""  # Define the global variable player outside of main()
max: int = 0
COIN_EMOJI: str = "\U0001FA99"


def greet() -> None:
    """Takes player name and introduces them to the game."""
    global player
    print("Welcome Player!")
    player = input("Enter your name: ")
    print(f"Hello, {player}! Welcome to the coin flip game! The goal of this game is to make as many consecutive correct guesses of a coin flip as possible!")


def guess_heads() -> None:
    """Player chooses heads or tails and are rewarded points if they guess correctly."""
    global points
    global COIN_EMOJI
    coin = random.choice(["heads", "tails"])
    guess = input(f"{player}, do you choose heads or tails?: ")
    if guess.lower() == coin:
        print(f"Congratulations! You guessed correctly {COIN_EMOJI}")
        points += 1
    else:
        print(f"Sorry, the coin was {coin}. Better luck next time.")
        points = 0


def double_down() -> None:
    """Player guesses heads or tails, if both coins are equal they are awarded points."""
    global points
    global COIN_EMOJI
    coin1: str = random.choice(["heads", "tails"])
    coin2: str = random.choice(["heads", "tails"])
    guess = input(player + ", do you choose heads or tails?: ")
    if guess.lower() == coin1 and coin2:
        print(f"Congratulations! You guessed correctly {COIN_EMOJI}")
        points += 4
    else:
        print(f"Sorry, the coins were {coin1} and {coin2}. Better luck next time.")
        points = 0


def high_score(current: int, maximum: int) -> int:
    """Determines player's high score."""
    if current > maximum:
        return current
    else:
        return maximum


def main() -> None:
    """Entry of program."""
    global points  # Declare points as a global variable within main()
    global max
    global player  # Declare player name as a global variable
    points = 0   # Initialize points to 0
    greet()
    while True:
        max = high_score(points, max)
        print(f"Adventure points: {points}")
        print("Choose your next adventure:")
        print("1. Guess heads or tails")
        print("2. Quadruple or nothing")
        print("3. End the experience")
        choice = input("Enter 1, 2, or 3: ")
        if choice == "1":
            guess_heads()
        elif choice == "2":
            double_down()
        elif choice == "3":
            if max == 1:
                print(f"Goodbye, {player}! Your high score was {max} adventure point! {COIN_EMOJI}")
            else:
                print(f"Goodbye, {player}! Your high score was {max} adventure points! {COIN_EMOJI}")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()