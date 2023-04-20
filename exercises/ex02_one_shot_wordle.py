"""EX02 - One Shot Wordle."""
__author__ = "730558551"

"""Defines word, user's word, and the output"""
secret_word: str = "python"
user_guess: str = input(f"What is your {len(secret_word)}-letter guess? ")
box_output: str = ""

"""Defines emojis"""
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

word_index: int = 0
tries: int = 0

"""Checks to make sure word is correct length"""
while (len(user_guess) != len(secret_word)):
    user_guess = input(f"That was not {len(secret_word)} letters! Try again: ")
        
"""Searches through indexes for matches and reports in output"""
if len(user_guess) == len(secret_word):
    while (word_index < (len(secret_word))):
        if user_guess[word_index] == secret_word[word_index]:
            box_output = box_output + GREEN_BOX
        elif user_guess[word_index] in secret_word:
            box_output = box_output + YELLOW_BOX
        else:
            box_output = box_output + WHITE_BOX
        word_index = word_index + 1
    print(box_output)
    if user_guess == secret_word:
        print("Woo! You got it!")
    if user_guess != secret_word:
        print("Not quite. Play again soon!")