# idea of the game is there is a secret word
# the user can interact with the game to guess the secret word
# they have 3 tries and then game ends

secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Guess the word I'm thinking: ")
        guess_count += 1
    else:
        out_of_guesses = True

if guess == secret_word:
    print("you win!")
else:
    print("you're out of guesses")
