class Card:
    def pay(self, amount):
        print("Paid", amount, "using Card")

class UPI:
    def pay(self, amount):
        print("Paid", amount, "using UPI")

class Cash:
    def pay(self, amount):
        print("Paid", amount, "using Cash")

class Payment:
    def __init__(self, strategy):
        self.strategy = strategy

    def process(self, amount):
        self.strategy.pay(amount)

p = Payment(UPI())
p.process(500)

p = Payment(Card())
p.process(1000)

p = Payment(Cash())
p.process(200)
