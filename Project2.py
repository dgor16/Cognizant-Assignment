import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print("You have 10 chances to guess it correctly.")

# Generate the secret number
number_to_guess = random.randint(1, 100)

# Initialize attempt counter
attempts = 0
max_attempts = 10

# Game loop
while attempts < max_attempts:
    print("\nAttempt", attempts + 1, ": Take a guess —")
    guess = int(input())
    attempts += 1

    if guess > number_to_guess:
        print("Too high! Try again.")
    elif guess < number_to_guess:
        print("Too low! Try again.")
    else:
        print("Congratulations! You guessed it!")
        print("You got it in", attempts, "attempts.")
        break

# If the player didn't guess in 10 attempts
if attempts == max_attempts and guess != number_to_guess:
    print("\nGame over! Better luck next time!")
    print("The number was:", number_to_guess)