from coins import Coin

class Wallet:
    def __init__(self):
        self.money = []
        self.fill_wallet = fill_wallet


def fill_wallet(self):
    """Method will fill wallet's money list with certain amount of each type of coin when called."""
    for index in range(8):
        self.money.append(Coin.Quarter())
    for index in range(10):
        self.money.append(Coin.Dime())
    for index in range(20):
        self.money.append(Coin.Nickel())
    for index in range(50):
        self.money.append(Coin.Penny())
