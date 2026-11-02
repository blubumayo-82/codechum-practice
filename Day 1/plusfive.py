nums = list(map(int, input().split()))

adjusted = []
maxed = 0

for x in nums:
    x = min(100, x + 5)
    if x == 100:
        maxed += 1
    adjusted.append(x)
     
print(*adjusted)
print(f"Maxed: {maxed}")