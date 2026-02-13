# Simple number guessing game

def guessing_game():
    # some variables
    # TODO: make random
    secret_number = 7
    attempts = 0
    max_attempts = 5

    while attempts < max_attempts:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess == secret_number:
            # exit function if correct
            print("Correct! You win.")
            return

        elif guess < secret_number:
            print("Too low.")

        else:
            print("Too high.")

        # debug
    # runs if loop finishes without correct guess
    print("Out of attempts. The number was", secret_number)

guessing_game()