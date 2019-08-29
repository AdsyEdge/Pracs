MINIMUM_LENGTH = 4


def main():
    password = get_password(MINIMUM_LENGTH)
    print(give_asterisk(password))


def get_password(minimum_length):
    password = input("Enter a password: ")
    while minimum_length > len(password):
        print("Error: Password length invalid! Password length must be at least 4.")
        password = input("Please enter a password: ")
    return password


def give_asterisk(password):
    return "*" * len(password)


main()
