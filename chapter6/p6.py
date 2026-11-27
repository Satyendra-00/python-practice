"""Assign a grade to a mark from zero through one hundred."""


def grade_for(marks):
    if not 0 <= marks <= 100:
        raise ValueError("marks must be between 0 and 100")
    if marks >= 90:
        return "A+"
    if marks >= 80:
        return "A"
    if marks >= 70:
        return "B"
    if marks >= 60:
        return "C"
    if marks >= 50:
        return "D"
    return "F"


def main():
    while True:
        try:
            marks = int(input("Enter your marks: ").strip())
            grade = grade_for(marks)
        except ValueError:
            print("Please enter a whole number from 0 to 100.")
            continue
        break
    print(f"Your grade is {grade}")


if __name__ == "__main__":
    main()
