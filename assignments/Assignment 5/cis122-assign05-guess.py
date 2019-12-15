'''
CIS 122 Fall 2018 Assignment 5
Author: Jacob I Rammer
Credit: N/A
Description: Word guessing game
'''


word = input("Enter a guess word (blank to quit): ")
word_guessed = False
guesses = 0  # Counts how many guesses its taken
guessed_chars = ''  # all the characters guessed
matched_char = ''  # if a character is matched to word
unmatched_char = ''  # if character does not match char in word
char_guess = ''
length = 0


while word_guessed is False:
    if len(word) == 0:
        break

    char_guess = input("Enter a guess letter (blank to quit): ").strip()
    if len(char_guess) == 0:
        break

    while len(char_guess) > 1:
        print("\t> Only enter a single letter")
        char_guess = input("Enter a guess letter (blank to quit): ")

    if char_guess in guessed_chars:
        if char_guess in word:
            print("\t> " + str(char_guess), "already guessed and found")
        elif char_guess not in word:
            print("\t> " + str(char_guess), "already guessed and not found")

    elif char_guess in word:
        guessed_chars += char_guess
        matched_char += char_guess
        print("\t> " + str(char_guess), "found")
        length += word.count(char_guess)  # Counts the number of times a char appears in word

    elif char_guess not in word:
        guessed_chars += char_guess
        unmatched_char += char_guess
        print("\t> " + str(char_guess), "not found")

    guesses += 1

    print("\t> Guesses fo far:", guessed_chars[::-1])  # Prints chars guessed already reversed.

    if length == len(word):
        # Have to tab align per assignment instructions
        print("*** Results ***\n" + "Word:\t\t", word, "\nMatched:\t", matched_char, "\nUnmatched:\t", unmatched_char,
              "\nGuesses:\t", guesses)
        word_guessed = True  # return True to exit the loop
