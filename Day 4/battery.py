arr = list(map(int, input("Enter cell voltages: ").split()))
k = int(input("Enter consecutive cells: "))

n = len(arr)
double_arr = arr + arr
curr = sum(arr[:k])
max_power = curr

for i in range(n - 1):
    curr = curr - double_arr[i] + double_arr[i + k]
    if curr > max_power:
        max_power = curr

print(f"Maximum power: {max_power}")
