"""Calculate the average of a non-empty collection of numbers."""


def average(numbers):
    numbers = tuple(numbers)
    if not numbers:
        raise ValueError("at least one number is required")
    return sum(numbers) / len(numbers)


def avg():
    count = int(input("Enter the number of elements: "))
    if count < 1:
        raise ValueError("the number of elements must be at least 1")
    values = [int(input("Enter number: ")) for _ in range(count)]
    return average(values)


def main():
    print("Average:", avg())


if __name__ == "__main__":
    main()