import random
MINIMUM = 0
MAXIMUM = 45
QUICK_PICK_LINE = 6


def main():
    pick_input = int(input("How many quick picks? "))
    for i in range(pick_input):
        quick_pick = []
        for r in range(QUICK_PICK_LINE):
            random_number = random.randint(MINIMUM, MAXIMUM)
            while random_number in quick_pick:
                random_number = random.randint(MINIMUM, MAXIMUM)
            quick_pick.append(random_number)
        quick_pick.sort()
        print(quick_pick)


main()
