"""EX02 - Structured Wordle."""
__author__ = "730558551"



def contains_char(SW : str, GSS : str) -> bool:
    """Checks if SW contains GSS"""
    assert len(GSS) == 1
    i: int = 0
    while i < len(SW):
        if GSS == SW[i]:
            return True
        i += 1
    return False

def emojified(GSS: str, SW: str) -> str:
    """Determines green, yellow, or white box"""
    assert len(SW) == len(GSS)
    result = ""
    index: int = 0
    # Box variables
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    while index < len(SW):
        if SW[index] == GSS[index]:
            result += GREEN_BOX
        else:
            # Checks for yellow
            Y_or_W: bool = False
            Y_or_W = contains_char(SW, GSS[index])
            if Y_or_W:
                result += YELLOW_BOX
            else:
                result += WHITE_BOX

            # if not green or yellow then white
        index += 1
    return result

def input_guess(expctd_lngth: int) -> str:
    """Checks if user's guess is the correct length"""
    guess: str = input("Enter a " + str(expctd_lngth) + " letter word: ")
    while len(guess) != expctd_lngth:
        guess = input("That wasn't " + str(expctd_lngth) + " chars! Try again: ") 
    return guess

def main() -> None:
    """Entry of program"""
    secret: str = "codes"
    length: int = len(secret)
    guess_count: int = 1
    guess: str = ""
    won: bool = False
    while guess_count <= 6:
        print("=== Turn " + str(guess_count) + " /6 ===")
        guess = input_guess(len(secret))
        print(emojified(guess, secret))
        if guess == secret:
            winning_turns: int = guess_count
            guess_count = 7
        else:
            guess_count += 1
    if guess == secret:
        print("You won in " + str(winning_turns) + " /6 turns!")
        won == True
    else:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()