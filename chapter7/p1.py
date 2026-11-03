"""Print the multiplication table for an integer."""


def multiplication_table(number, limit=10):
    return [
        f"{number} x {multiplier} = {number * multiplier}"
        for multiplier in range(1, limit + 1)
    ]


def main():
    while True:
        raw_number = input("Enter an integer: ").strip()
        try:
            number = int(raw_number)
        except ValueError:
            print("Please enter a whole number.")
            continue
        break

    for row in multiplication_table(number):
        print(row)


if __name__ == "__main__":
    main()
