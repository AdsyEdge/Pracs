CURRENT_YEAR = 2019
VINTAGE_AGE = 50


class Guitar:
    def __init__(self, name, year, cost):
        self.name = name
        self.year = year
        self.cost = cost

    def __str___(self):
        return "{} ({}) : ${}".format(self.name, self.year, self.cost)

    def get_age(self):
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        return self.get_age() >= VINTAGE_AGE
