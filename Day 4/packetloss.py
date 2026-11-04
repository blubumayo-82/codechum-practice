arr = list(map(int, input("Enter packet drops: ").split()))
k = int(input("Enter duration: "))

curr = sum(arr[:k])
min_sum = curr

for i in range(len(arr) - k):
    curr = curr - arr[i] + arr[i + k]

    if min_sum > curr:
        min_sum = curr

print(f"Minimum loss: {min_sum}")