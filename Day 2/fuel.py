d = float(input("Enter distance in km: "))
a = float(input("Enter fuel for Car A in L: "))
b = float(input("Enter fuel for Car B in L: "))
eff_a = d/a
eff_b = d/b

if eff_a > eff_b:
    p = ((eff_a - eff_b)/eff_b) * 100
    print(f"Car A is more efficient by {p:.2f}%")
elif eff_a < eff_b:
    p = ((eff_b - eff_a)/eff_a) * 100
    print(f"Car B is more efficient by {p:.2f}%")
else:
    print("Both cars have the same efficiency")