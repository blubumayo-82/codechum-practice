n = int(input())

for _ in range(n):
    name, wage, hour = input().split()
    pay = float(wage) * float(hour)
    print(f"{name}: ${pay:.2f}")