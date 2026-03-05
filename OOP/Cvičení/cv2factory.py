from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CardPayment(Payment):
    def pay(self, amount):
        print(f"Zaplaceno {amount} kartou")

class CashPayment(Payment):
    def pay(self, amount):
        print(f"Zaplaceno {amount} hotove")

def payment_factory(payment_type):
    types = {
        "card": CardPayment(),
        "cash": CashPayment()
    }
    return types.get(payment_type)


class PaymentProcessor:
    def pay(self, payment_type, amount):
        obj = payment_factory(payment_type)
        if obj:
            obj.pay(amount)
        else:
            print("Neznamy typ platby")


if __name__ == "__main__":
    processor = PaymentProcessor()
    processor.pay("card", 100)
    processor.pay("cash", 300)
    processor.pay("coin", 50)