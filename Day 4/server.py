arr = list(map(int, input("Enter request sizes: ").split()))
max_val = int(input("Enter max data: "))

left = 0
curr = 0
best = 0

for right in range(len(arr)):
    curr += arr[right]

    while curr > max_val:
        curr -= arr[left]
        left += 1

    best = max(best, right - left + 1)

print(f"Max consecutive requests: {best}")