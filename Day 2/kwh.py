kwh = float(input("Enter kWh consumed: "))

if kwh <= 100:
    bill = kwh * 10.00
elif kwh <= 250:
    bill = (100 * 10) + ((kwh - 100) * 15.50)
else: 
    bill = (100 * 10) + ((250 - 100) * 15.50) + ((kwh - 250) * 20.00)

if bill > 3000:
    bill = bill * 1.05

print(f"Total Bill: PHP {bill:.2f}")