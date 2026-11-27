"""Check whether a student passes based on three subject marks."""


def passed(marks):
    """Return whether all marks are at least 33 and the total is 120+."""
    marks = tuple(marks)
    if len(marks) != 3 or any(not 0 <= mark <= 100 for mark in marks):
        raise ValueError("provide exactly three marks from 0 to 100")
    return all(mark >= 33 for mark in marks) and sum(marks) >= 120


def main():
    while True:
        try:
            marks = [
                int(input(f"Enter your marks in {subject}: ").strip())
                for subject in ("Hindi", "English", "Maths")
            ]
            result = passed(marks)
        except ValueError:
            print("Please enter whole number marks from 0 to 100.")
            continue
        break

    print("You are pass" if result else "You are fail")


if __name__ == "__main__":
    main()
