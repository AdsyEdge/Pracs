
def main():
    score = float(input("Enter score: "))
    print(validate_score(score))


def validate_score(score):
    if score < 0 or score > 100:
        return "Invalid score."
    elif score < 50:
        return "Bad."
    elif 90 > score >= 50:
        return "Passable."
    else:
        return "Excellent."


main()
