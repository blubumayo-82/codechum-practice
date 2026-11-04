arr = list(map(int, input("Enter signal values: ").split()))
k = int(input("Enter window size: "))

current_sum = sum(arr[:k])
max_sum = current_sum

for i in range(len(arr) - k):
    current_sum = current_sum - arr[i] + arr[i + k]

    if current_sum > max_sum:
        max_sum = current_sum

print(f"Maximum signal: {max_sum}")