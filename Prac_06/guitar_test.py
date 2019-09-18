from Prac_06.guitar import Guitar

name = "Gibson L-5 CES"
year = 1922
cost = 16035.40
guitar_details = Guitar(name, year, cost)
guitar_test = Guitar("Another Guitar", 2012, 209.50)
print("{} get_age() - Expected {}. Got {}".format(guitar_details.name, 97, guitar_details.get_age()))
print("{} get_age() - Expected {}. Got {}".format(guitar_test.name, 7, guitar_test.get_age()))
print("{} is_vintage() - Expected {}. Got {}".format(guitar_details.name, True, guitar_details.is_vintage()))
print("{} is_vintage() - Expected {}. Got {}".format(guitar_test.name, False, guitar_test.is_vintage()))
