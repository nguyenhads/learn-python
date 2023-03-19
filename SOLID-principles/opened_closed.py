# =========================== BEFORE ===========================

class Order:
    
    def __init__(self):
        self.items = []
        self.quantities = []
        self.prices = []
        self.status = "open"

    def add_item(self, name, quantity, price):
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

    def total_price(self):
        total = 0
        for i in range(len(self.prices)):
            total += self.quantities[i] * self.prices[i]
        return total


class Payment:
    
    def pay_debit(self, security_code):
        print(f"Verifying security code: {security_code}")
        self.status = "paid"
    
    def pay_credit(self, security_code):
        print(f"Verifying security code: {security_code}")
        self.status = "paid"


order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB cable", 2, 5)

payment = Payment()
print(order.items)
print(order.total_price())
payment.pay_debit("0372846")


# =========================== AfTER ===========================
# from abc import ABC, abstractmethod


# class Order():
    
#     def __init__(self):
#         self.items = []
#         self.quantities = []
#         self.prices = []
#         self.status = "open"

#     def add_item(self, name, quantity, price):
#         self.items.append(name)
#         self.quantities.append(quantity)
#         self.prices.append(price)

#     def total_price(self):
#         total = 0
#         for i in range(len(self.prices)):
#             total += self.quantities[i] * self.prices[i]
#         return total


# class PaymentBase(ABC):
#     @abstractmethod
#     def pay(self, order, security_code):
#         raise NotImplementedError


# class PayDebit(PaymentBase):
    
#     def pay(self, order, security_code):
#         print(f"Verifying security code: {security_code}")
#         order.status = "paid"


# class PayCredit(PaymentBase):
    
#     def pay(self, order, security_code):
#         print(f"Verifying security code: {security_code}")
#         order.status = "paid"

# # if we want to add net payment methods, we don't have to change the PaymentBase
# class PayPaypal(PaymentBase):
    
#     def pay(self, order, security_code):
#         print(f"Verifying security code: {security_code}")
#         order.status = "paid"       


# order = Order()
# order.add_item("Keyboard", 1, 50)
# order.add_item("SSD", 1, 150)
# order.add_item("USB cable", 2, 5)

# print(order.items)
# print(order.total_price())
# payment = PayPaypal()
# payment.pay(order, "0372846")
