class Item:
    def __init__(self, name: str, price: float, quantity: int = 1):
        if price < 0:
            raise ValueError("Price cannot be negative.")
        if quantity <= 0:
            raise ValueError("Quantity must be at least 1.")
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_total_price(self) -> float:
        return round(self.price * self.quantity, 2)


class BillingSystem:
    def __init__(self, tax_rate: float = 0.05):
        """
        tax_rate: 0.05 represents 5% tax
        """
        if tax_rate < 0:
            raise ValueError("Tax rate cannot be negative.")
        self.tax_rate = tax_rate
        self.items = []

    def add_item(self, item: Item):
        self.items.append(item)

    def calculate_subtotal(self) -> float:
        return round(sum(item.get_total_price() for item in self.items), 2)

    def calculate_tax(self, discount: float = 0.0) -> float:
        subtotal = self.calculate_subtotal()
        discounted_amount = max(0.0, subtotal - discount)
        return round(discounted_amount * self.tax_rate, 2)

    def calculate_grand_total(self, discount: float = 0.0) -> float:
        subtotal = self.calculate_subtotal()
        if discount < 0 or discount > subtotal:
            raise ValueError("Invalid discount value.")
        
        tax = self.calculate_tax(discount)
        return round((subtotal - discount) + tax, 2)


if __name__ == "__main__":
    bill = BillingSystem(tax_rate=0.05)
    bill.add_item(Item("Notebook", 40.0, 2))
    bill.add_item(Item("Pen", 10.0, 3))
    
    subtotal = bill.calculate_subtotal()
    total = bill.calculate_grand_total(discount=10.0)
    
    print(f"Subtotal: Rs. {subtotal}")
    print(f"Grand Total (with 5% tax & Rs. 10 discount): Rs. {total}")
