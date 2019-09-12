"""CP1404/CP5632 Practical - Client code to use the Car class."""
# Note that the import has a folder (module) in it.

from Prac_06.car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car("Car", 180)
    my_car.drive(int(30))
    print("fuel =", my_car.fuel)
    print("odometer =", my_car.odometer)
    print(my_car)

    print("{} {}, {}".format(my_car, my_car.fuel, my_car.odometer))
    print("{} {self.fuel}, {self.odometer}".format(my_car, self=my_car))

    limo = Car("Limo", 100)
    limo.add_fuel(int(20))
    print("fuel =", limo.fuel)
    limo.drive(115)
    print("odometer =", limo.odometer)

    print("{} {}, {}".format(limo, my_car.fuel, my_car.odometer))
    print("{} {self.fuel}, {self.odometer}".format(limo, self=my_car))


main()
