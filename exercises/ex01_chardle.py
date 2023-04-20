"""EX01 - Chardle - A cute step toward Wordle."""
__author__ = "730558551"

"""Define a valid word and letter"""
word: str = input("Enter a 5-character word: ")
if len(word) != 5:
    print("Error: Word must contain 5 characters")
    exit()
letter: str = input("Enter a single character: ")
if len(letter) != 1:
    print("Error: Character must be a single character.")
    exit()
print("Searching for " + letter + " in " + word)

"""Number of times letter appears in word"""
instances_count: int = 0

"""Check each index for user-chosen letter"""
if word[0] == letter:
    print(letter + " found at index 0")
    instances_count += 1
if word[1] == letter:
    print(letter + " found at index 1")
    instances_count += 1
if word[2] == letter:
    print(letter + " found at index 2")
    instances_count += 1
if word[3] == letter:
    print(letter + " found at index 3")
    instances_count += 1
if word[4] == letter:
    print(letter + " found at index 4")
    instances_count += 1

"""Output result of number of letter instances"""
if instances_count == 0:
    print("No instances of " + letter + " found in " + word)
elif instances_count == 1:
    print(str(instances_count) + " instance of " + letter + " found in " + word)
else:
    print(str(instances_count) + " instances of " + letter + " found in " + word)