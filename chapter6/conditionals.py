"""Check whether someone meets the voting age."""


def is_eligible_to_vote(age):
    return age >= 18


def main():
    while True:
        try:
            age = int(input("Enter your age: ").strip())
        except ValueError:
            print("Please enter your age as a whole number.")
            continue

        if age < 0:
            print("Age cannot be negative.")
            continue
        break

    if is_eligible_to_vote(age):
        print("You are eligible to vote.")
    else:
        print("You are not eligible to vote.")


if __name__ == "__main__":
    main()
