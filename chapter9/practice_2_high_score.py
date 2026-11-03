"""Play a small quiz and save a new high score."""

from pathlib import Path

HIGH_SCORE_FILE = Path("Hi-score.txt")


def game():
    score = 0

    answer = input("What is 2 + 2? ").strip()
    if answer == "4":
        score += 10

    answer = input("What is the capital of India? ").strip().lower()
    if answer == "new delhi":
        score += 10

    return score


def load_high_score(path=HIGH_SCORE_FILE):
    try:
        saved_score = path.read_text(encoding="utf-8").strip()
        return int(saved_score) if saved_score else 0
    except FileNotFoundError:
        return 0
    except ValueError:
        print("The saved high score is invalid. Starting from 0.")
        return 0


def main():
    score = game()
    print(f"Your score: {score}")

    high_score = load_high_score()
    if score > high_score:
        HIGH_SCORE_FILE.write_text(str(score), encoding="utf-8")
        print("New high score!")
    else:
        print(f"The high score is still {high_score}.")


if __name__ == "__main__":
    main()
