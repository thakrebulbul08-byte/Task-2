import random

def guess_the_number():
    print("\n🎮 Welcome to the Guess the Number Game!")
    print("I have selected a number between 1 and 100.")

    number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("\nEnter your guess: "))

            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
                continue

            attempts += 1

            if guess < number:
                print("Too Low! Try again.")
            elif guess > number:
                print("Too High! Try again.")
            else:
                print(f"🎉 Correct! You guessed the number in {attempts} attempts.")
                break

        except ValueError:
            print("Invalid input! Please enter a valid integer.")

    play_again = input("\nDo you want to play again? (yes/no): ").lower()

    if play_again == "yes":
        guess_the_number()
    else:
        print("Thank you for playing! Goodbye! 👋")


guess_the_number()
