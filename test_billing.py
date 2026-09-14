import pytest
from billing import Item, BillingSystem

def test_item_total():
    item = Item("Keyboard", 500.0, 2)
    assert item.get_total_price() == 1000.0

def test_invalid_item_price():
    with pytest.raises(ValueError):
        Item("InvalidItem", -10.0, 1)

def test_invalid_item_quantity():
    with pytest.raises(ValueError):
        Item("InvalidItem", 50.0, 0)

def test_bill_calculation_without_discount():
    bill = BillingSystem(tax_rate=0.10)
    bill.add_item(Item("Book", 100.0, 1))
    
    assert bill.calculate_subtotal() == 100.0
    assert bill.calculate_grand_total() == 110.0

def test_bill_calculation_with_discount():
    bill = BillingSystem(tax_rate=0.05)
    bill.add_item(Item("Shirt", 500.0, 2))
    
    assert bill.calculate_grand_total(discount=200.0) == 840.0

def test_invalid_discount():
    bill = BillingSystem(tax_rate=0.05)
    bill.add_item(Item("Pen", 20.0, 1))
    
    with pytest.raises(ValueError):
        bill.calculate_grand_total(discount=50.0)
