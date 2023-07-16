#!/usr/bin/env python3


class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total_cost = 0
        self.cart = []

    def add_item(self, item, price, quantity=1):
        self.total_cost += price * quantity
        for i in range(quantity):
            self.cart.append((item, price))

    def apply_discount(self):
        if self.total_cost > 0:
            self.total_cost -= self.total_cost * self.discount / 100
            print(f"After the discount, the total comes to ${int(self.total_cost)}.")
        else:
            print(f"There is no discount to apply.")

    #Subracts the last serveral items of the same name from the cart. Also subtracts the sum of the prices of the items from the total cost.
    def void_last_transaction(self):
        if self.cart:
            name = self.cart[-1][0]
            while self.cart and self.cart[-1][0] == name:
                item, price = self.cart.pop()
                self.total_cost -= price     

    #Gets the names of the items in the cart.
    def get_items(self):
        return [item for item, _ in self.cart]
    
    def get_total(self):
        return self.total_cost
    
    items = property(get_items)
    total = property(get_total)
