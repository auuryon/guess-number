import random

tries = {
    1: 10,
    2: 5,
    3: 3
}

level_difficult = {
    1: "Easy",
    2: "Medium",
    3: "Hard"
}

def init_game():
    roll_number = random.randint(1,100)

    print(f"""
    Welcome to the Number Guessing Game!
    I'm thinking of a number between 1 and 100.
    """)

    difficult = int(input("""Please select the difficulty level:
    1. Easy (10 chances)
    2. Medium (5 chances)
    3. Hard (3 chances)

    Enter your choice: """))

    print(f"""
    Great! You have selected the {level_difficult[difficult]} difficulty level.
    Let's start the game!
    You have {tries[difficult]} chances to guess the correct number.
    """)

    total_tries = tries[difficult]

    while tries[difficult] != 0:
        guess_number = int(input("Enter your guess: "))

        if guess_number > roll_number:
            tries[difficult] -= 1
            print(f"Incorrect! The number is less than {guess_number}.\n")
        elif guess_number < roll_number:
            tries[difficult] -= 1
            print(f"Incorrect! The number is greater than {guess_number}.\n")
        else:
            tries[difficult] -= 1
            print(f"Congratulations! You guessed the correct number in {total_tries - tries[difficult]} attempts.\n")
            break

        if tries[difficult] == 0:
            print("Unfortunately, your attemps have ended.\n")

    continue_guess = int(input("""You want to play again?
    1. Yes
    2. No
    """))

    if continue_guess == 1:
        init_game()
    else:
        quit()

init_game()