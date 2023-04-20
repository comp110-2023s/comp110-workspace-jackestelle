"""EX03 - Structured Wordle."""
__author__ = "730558551"



def contains_char(WD : str, GS : str) -> bool:
    """Checks if WD contains GS"""
    assert len(GS) == 1
    i: int = 0
    while i < len(WD):
        if GS == WD[i]:
            return True
        i += 1
    return False

def emojified(GS: str, WD: str) -> str:
    """Determines green, yellow, or white box"""
    assert len(WD) == len(GS)
    boxes = ""
    ind: int = 0
    # Creates variables of emojis
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    while ind < len(WD):
        if WD[ind] == GS[ind]:
            boxes += GREEN_BOX
        else:
            # determines if yellow emoji is appropriate
            Y_or_W: bool = False
            Y_or_W = contains_char(WD, GS[ind])
            if Y_or_W:
                boxes += YELLOW_BOX
            else:
                boxes += WHITE_BOX

            # White Box
        ind += 1
    return boxes

def input_guess(word_len: int) -> str:
    """Checks if user's guess is the correct length"""
    guess: str = input("Enter a " + str(word_len) + " character word: ")
    while len(guess) != word_len:
        guess = input("That wasn't " + str(word_len) + " chars! Try again: ") 
    return guess

def main() -> None:
    """Entry of program"""
    word: str = "codes"
    length: int = len(word)
    guess_ct: int = 1
    guess: str = ""
    win: bool = False
    while guess_ct <= 6:
        print("=== Turn " + str(guess_ct) + "/6 ===")
        guess = input_guess(len(word))
        print(emojified(guess, word))
        if guess == word:
            winning_turns: int = guess_ct
            guess_ct = 7
        else:
            guess_ct += 1
    if guess == word:
        print("You won in " + str(winning_turns) + "/6 turns!")
        win == True
    else:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()