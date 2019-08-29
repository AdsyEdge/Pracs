def main():
    """
    Basic List Operations
    """
    numbers = []
    for i in range(5):
        number_input = int(input("Enter your number: "))
        numbers.append(number_input)
    print("The first number is:", numbers[0])
    print("The last number is:", numbers[-1])
    print("The smallest number is:", min(numbers))
    print("The largest number is:", max(numbers))
    print("The average of the numbers is:", sum(numbers)/5)

    """
    Woefully inadequate security checker
    """
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']
    username_input = input("Please enter a username: ")
    if username_input in usernames:
        print("Access Granted.")
    else:
        print("Access Denied.")


main()
