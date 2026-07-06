def is_palindrome_number(number):
    if number < 0:
        return False

    original = number
    reversed_number = 0

    while number > 0:
        digit = number % 10
        reversed_number = reversed_number * 10 + digit
        number = number // 10

    return original == reversed_number


def main():
    number = int(input("give the number to check if it polindrome: "))
    result = is_palindrome_number(number)
    print(result)


if __name__ == "__main__":
    main()