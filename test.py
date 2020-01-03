# this is my failure of a hangman game
# sets secret word
secret_word = "hello"

# replaces secret word with dashes and prints
dashes = "-" * len(secret_word)
print dashes

# takes user's guess
guess = input("Guess: ")

# the bane of my existence (incomplete)
def update_dashes(secret_word, dashes, guess):
    for i in range(len(secret_word)):
        if secret_word[i] == guess:
            dashes = dashes[:i] + guess + dashes[i + 1:]
    return dashes


# determines if the guess is
# 1. valid, and
# 2. whether it's correct or not

def get_guess(guess):
    while True:
        if len(guess) > 1:
            print "Your guess must have exactly one character."
            guess = input("Guess: ")
        elif not guess.islower():
            print "Your guess must be a lowercase letter."
            guess = input("Guess: ")
        elif guess in secret_word:
            print "That letter is in the secret word!"
            print update_dashes(secret_word, dashes, guess)
            guess = input("Guess: ")
        else:
            print "That letter is not in the secret word."
            print dashes
            guess = input("Guess: ")
get_guess(guess)
