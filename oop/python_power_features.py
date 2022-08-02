class Payment:
    def __new__(cls, payment_type: str):
        if payment_type == "Paypal":
            return object.__new__(PaypalPayment)
        elif payment_type == "Stripe":
            return object.__new__(StripePayment)

    def pay(self, amount: int) -> None:
        raise NotImplementedError


class PaypalPayment(Payment):
    def pay(self, amount: int) -> None:
        print(f"Paying {amount} using Paypal")


class StripePayment(Payment):
    def pay(self, amount: int) -> None:
        print(f"Paying {amount} using Stripe")


def main() -> None:
    my_payment = Payment("Paypal")
    my_payment1 = Payment("Stripe")
    print("==>> my_payment == my_payment1: ", my_payment == my_payment1) # False
    if my_payment1:
        my_payment1.pay(amount=100)
    if my_payment:
        my_payment.pay(amount=20000)

print(Payment.__dict__)

if __name__ == "__main__":
    main()