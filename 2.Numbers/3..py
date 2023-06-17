import random

def guess_number():
    random_number = random.randint(1, 100)
    attempts = 0

    while True:
        guess = int(input("Guess a number between 1 and 100: "))
        attempts += 1

        if guess == random_number:
            print("Congratulations! You guessed the correct number.")
            break
        elif guess < random_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

    return attempts

total_attempts = guess_number()
print("Total attempts:", total_attempts)