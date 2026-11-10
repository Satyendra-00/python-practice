def greatest_of_three(a,b,c):
    return max(a, b, c)


def main():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = int(input("Enter third number: "))
    print("Greatest of three numbers is:", greatest_of_three(a, b, c))


if __name__ == "__main__":
    main()