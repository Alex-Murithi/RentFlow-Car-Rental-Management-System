from abc import ABC, abstractmethod
import random, string

class Payment(ABC):
    def __init__(self, rental):
        if rental.is_paid():
            raise ValueError("Rental already paid.")
        self.rental = rental
        self.amount = rental.calculate_total()

    @abstractmethod
    def process_payment(self):
        pass


class MpesaPayment(Payment):
    def __init__(self, rental, phone_number):
        super().__init__(rental)
        self.phone_number = phone_number

    def process_payment(self):
        code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
        print("Processing M-Pesa payment...")
        print(f"Transaction: {code}")
        print(f"Payment of KSh {self.amount} successful.")
        self.rental.mark_as_paid()
        return True


class CardPayment(Payment):
    def __init__(self, rental, card_last4):
        super().__init__(rental)
        self.card_last4 = card_last4

    def process_payment(self):
        print(f"Card ending {self.card_last4} charged KSh {self.amount}")
        self.rental.mark_as_paid()
        return True


class CashPayment(Payment):
    def __init__(self, rental, cash_received):
        super().__init__(rental)
        self.cash_received = cash_received

    def process_payment(self):
        if self.cash_received < self.amount:
            print("Cash payment failed: insufficient funds.")
            return False
        change = self.cash_received - self.amount
        print(f"Cash received: KSh {self.cash_received}")
        print(f"Change due:    KSh {change}")
        print(f"Cash payment of KSh {self.amount} recorded.")
        self.rental.mark_as_paid()
        return True
