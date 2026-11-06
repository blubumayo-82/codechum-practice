arr = list(map(int, input("Enter cell outputs: ").split()))
target = int(input("Enter target power: "))

left = 0
curr = 0
best = float('inf')

for right in range(len(arr)):
    curr += arr[right]

    while curr >= target:
        best = min(best, right - left + 1) 
        curr -= arr[left]
        left += 1

if best == float('inf'):
    best = 0
print(f"Min cells required: {best}")