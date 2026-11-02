item_id, unit_price, quantity, discount_rate =  input().split()
unit_price = float(unit_price)
quantity = int(quantity)
discount_rate = float(discount_rate)

subtotal = unit_price * quantity
discount = subtotal * (discount_rate / 100)
total = subtotal - discount

print(f"Item: {item_id}")
print(f"Total: {total:.2f}")

