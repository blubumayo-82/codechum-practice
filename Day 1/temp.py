n = int(input())
temp = [float(input()) for _ in range(n)]

h = max(temp)
l = min(temp)
a = sum(temp)/n

print(f"Average: {a:.2f}")
print(f"Highest: {h:.2f}")
print(f"Lowest: {l:.2f}")

