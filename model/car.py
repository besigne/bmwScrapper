class Car:

    def __init__(self, name, price, fuel):
        self.__name = name
        self.__fuel = fuel
        self.__price = price

    @property
    def name(self):
        return self.__name

    @property
    def fuel(self):
        return self.__fuel

    @property
    def price(self):
        return self.__price
