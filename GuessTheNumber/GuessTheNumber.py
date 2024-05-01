from random import randint


def game():
    print("Welcome to the Number Guessing Game!\nI am thinking of a number between 1 and 100")
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    tries = 10 if level == "easy" else 5
    guess_the_number = randint(1, 100)
    print(guess_the_number)
    player_guess = int(input("Guess the number: "))
    while tries:

        if player_guess == guess_the_number:
            print(f"Congratulation! The number was {player_guess}")
            return

        if player_guess > guess_the_number:
            print("Too high.\nGuess again.")
        else:
            print("Too low.\nGuess again.")

        player_guess = int(input("Guess the number: "))
        tries -= 1
        print(f"Remaining entries: {tries}")

    print("You have no more tries left. You lost.")
    return


game()
