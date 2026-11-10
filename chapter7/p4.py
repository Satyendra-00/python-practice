"""Check whether an integer is prime."""

from math import isqrt


def is_prime(number):
    if number < 2:
        return False
    return all(number % divisor for divisor in range(2, isqrt(number) + 1))


def main():
    number = int(input("Enter a number: "))
    print("Prime number" if is_prime(number) else "Not a prime number")


if __name__ == "__main__":
    main()