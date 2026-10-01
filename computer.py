class Computer:
    def __init__(self):
        self.__max = 100
    def sell(self):
        print("Selling price: {}".format(self.__max))
    def setMax(self, price):
        self.__max = price
c = Computer()
c.sell()

c.__max = 200
c.sell()

c.setMax(200)
c.sell()