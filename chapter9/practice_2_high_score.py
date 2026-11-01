"""Play a small quiz and save a new high score."""

import os


def game():
    score = 0

    answer = input("What is 2 + 2? ").strip()
    if answer == "4":
        score += 10

    answer = input("What is the capital of India? ").strip().lower()
    if answer == "new delhi":
        score += 10

    return score


score = game()
print(f"Your score: {score}")

file_name = "Hi-score.txt"
high_score = 0

if os.path.exists(file_name):
    with open(file_name, "r", encoding="utf-8") as file:
        saved_score = file.read().strip()
        if saved_score:
            try:
                high_score = int(saved_score)
            except ValueError:
                print("The saved high score is invalid. Starting from 0.")

if score > high_score:
    with open(file_name, "w", encoding="utf-8") as file:
        file.write(str(score))
    print("New high score!")
else:
    print(f"The high score is still {high_score}.")
