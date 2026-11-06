arr = list(map(int, input("Enter packet sequence: ").split()))

left = 0
curr = 0
best = 0
zero_count = 0

for right in range(len(arr)):
    if arr[right] == 0:
        zero_count += 1

    while zero_count > 1:
        if arr[left] == 0:
            zero_count -= 1
        left += 1

    best = max(best, right - left + 1)

print(f"Longest valid burst: {best}")