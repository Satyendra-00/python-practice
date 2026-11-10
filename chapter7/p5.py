"""Sum the integers from zero through a non-negative input."""


def sum_to(number):
    if number < 0:
        raise ValueError("number must be non-negative")
    return number * (number + 1) // 2


def main():
    number = int(input("Enter a non-negative integer: "))
    print(sum_to(number))


if __name__ == "__main__":
    main()