import random

print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 and 100.")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
random_choice = random.randint(1, 100)

def game(difficulty, random_choice):
    if difficulty == 'easy':
        total_attempts = 10
    elif difficulty == 'hard':
        total_attempts = 5
    else:
        print("Invalid difficulty.")
        return

    while total_attempts > 0:
        print(f"\nYou have {total_attempts} attempts remaining to guess the number.")
        user_choice = int(input("Make a guess: "))

        if user_choice > random_choice:
            print("Too high.")
        elif user_choice < random_choice:
            print("Too low.")
        else:
            print("You got it! You win!")
            return  # Sale de la función cuando adivina bien

        total_attempts -= 1

    print(f"\nYou've run out of guesses. You lose. The number was {random_choice}.")

game(difficulty, random_choice)
