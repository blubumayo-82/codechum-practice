b = float(input("Enter base cost: "))
p = float(input("Enter markup percentage: "))
sku = input("Enter item SKU string: ")

retail = b + (b * (p / 100))

if sku[0].isupper():
    retail *= 1.12

print(f"Final Retail Price: PHP {retail:.2f}")