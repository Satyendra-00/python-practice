"""Play a round of snake, water, gun."""

import random

CHOICES = {1: "snake", 2: "water", 3: "gun"}


def get_choice():
    while True:
        raw_choice = input("Enter your choice (1: snake, 2: water, 3: gun): ").strip()
        try:
            choice = int(raw_choice)
        except ValueError:
            print("Please enter a number: 1, 2, or 3.")
            continue

        if choice in CHOICES:
            return choice
        print("Choice must be 1, 2, or 3.")


def play_round(user_choice, computer_choice):
    if user_choice not in CHOICES or computer_choice not in CHOICES:
        raise ValueError("choices must be 1, 2, or 3")
    if user_choice == computer_choice:
        return "It's a draw."

    user_wins = {
        (1, 2),  # snake drinks water
        (2, 3),  # water rusts gun
        (3, 1),  # gun defeats snake
    }
    return "You win!" if (user_choice, computer_choice) in user_wins else "You lose."


def main():
    user_choice = get_choice()
    computer_choice = random.choice(tuple(CHOICES))
    print(f"You chose {CHOICES[user_choice]}; computer chose {CHOICES[computer_choice]}.")
    print(play_round(user_choice, computer_choice))


if __name__ == "__main__":
    main()
