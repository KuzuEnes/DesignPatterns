# Strategy Arayüzü
class PaymentStrategy:
    def pay(self, amount):
        pass

# Concrete Strategy 1
class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"{amount} TL kredi kartı ile ödendi.")

# Concrete Strategy 2
class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"{amount} TL PayPal ile ödendi.")

# Concrete Strategy 3
class CryptoPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"{amount} TL kripto para ile ödendi.")

# Context
class ShoppingCart:
    def __init__(self, payment_strategy: PaymentStrategy):
        self.payment_strategy = payment_strategy
        self.total = 0

    def add_item(self, price):
        self.total += price

    def checkout(self):
        self.payment_strategy.pay(self.total)

# Kullanım
cart1 = ShoppingCart(CreditCardPayment())
cart1.add_item(100)
cart1.add_item(50)
cart1.checkout()   # 150 TL kredi kartı ile ödendi.

cart2 = ShoppingCart(CryptoPayment())
cart2.add_item(200)
cart2.checkout()   # 200 TL kripto para ile ödendi.

#CreditCardPayment, PayPalPayment, CryptoPayment: Farklı stratejiler.
#ShoppingCart: Stratejiyi kullanarak işlemi gerçekleştirir. Stratejiyi çalışma zamanında değiştirebiliriz.

