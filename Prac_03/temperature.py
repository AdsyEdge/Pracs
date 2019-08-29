MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""


def main():
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = get_celsius_to_fahrenheit(celsius)
            print("Result: {:.2f} F".format(fahrenheit))
        elif choice == "F":
            celsius = get_fahrenheit_to_celsius()
            print("Result: {:.2f} C".format(celsius))
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")
    return True


def get_celsius_to_fahrenheit(celsius):
    return celsius * 9.0 / 5 + 32


def get_fahrenheit_to_celsius():
    fahrenheit = float(input("Fahrenheit: "))
    return 5 / 9 * (fahrenheit - 32)


main()
