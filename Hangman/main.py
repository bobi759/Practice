from random import choice

from Hangman.hangman_images_logo import HANGMAN_PICS, HANGMAN_LOGO
from Hangman.hangman_word_list import word_list

end_of_game = False
lives = 6
chosen_word = choice(word_list)
word_progress = ["_"] * len(chosen_word)

print(HANGMAN_LOGO)

while not end_of_game:
    guess = input("Guess a letter in the word: ").lower()

    if guess not in chosen_word.lower():
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
    if guess in word_progress:
        print("You already guessed that letter. Please try with another one.")
    else:
        for i in range(len(chosen_word)):
            if guess == chosen_word[i].lower():
                word_progress[i] = chosen_word[i]

    print(" ".join(word_progress))
    print(HANGMAN_PICS[len(HANGMAN_PICS) - 1 - lives])

    if "_" not in word_progress or lives == 0:
        end_of_game = True
        print(f"You lose. The word was {chosen_word}.")
