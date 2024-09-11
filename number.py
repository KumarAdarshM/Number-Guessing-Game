import random
import time

def welcome_message():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("You need to guess the number correctly to win.")
    print("You have a limited number of chances depending on the difficulty level.\n")

def select_difficulty():
    print("Please select the difficulty level:")
    print("1. Easy (10 chances)")
    print("2. Medium (5 chances)")
    print("3. Hard (3 chances)")
    
    while True:
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                return 10
            elif choice == 2:
                return 5
            elif choice == 3:
                return 3
            else:
                print("Invalid choice! Please select a valid difficulty level.")
        except ValueError:
            print("Invalid input! Please enter a number.")

def play_game():
    random_number = random.randint(1, 100)
    chances = select_difficulty()
    attempts = 0
    start_time = time.time()

    print(f"\nGreat! You have {chances} chances to guess the number. Let's start the game!\n")

    while attempts < chances:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess == random_number:
                end_time = time.time()
                print(f"Congratulations! You guessed the correct number in {attempts} attempts.")
                print(f"It took you {round(end_time - start_time, 2)} seconds to guess the number.")
                return attempts
            elif guess > random_number:
                print("Incorrect! The number is less than your guess.")
            else:
                print("Incorrect! The number is greater than your guess.")

            print(f"You have {chances - attempts} chances left.\n")
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    print(f"Sorry! You've run out of chances. The correct number was {random_number}.")
    return None

def play_again():
    while True:
        choice = input("Do you want to play again? (yes/no): ").lower()
        if choice == 'yes':
            return True
        elif choice == 'no':
            return False
        else:
            print("Invalid input! Please enter 'yes' or 'no'.")

def main():
    welcome_message()
    high_score = None
    
    while True:
        attempts = play_game()
        
        if attempts and (high_score is None or attempts < high_score):
            high_score = attempts
            print(f"New high score: {high_score} attempts!\n")

        if not play_again():
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()
