arr = list(map(int, input("Enter signal values: ").split()))
k = int(input("Enter window size: "))

# The first window - solve it.
current_sum = sum(arr[:k])
max_sum = current_sum

# loop starts array - k
for i in range(len(arr) - k):
    # current_sum - the previous first in the window + the next number
    current_sum = current_sum - arr[i] + arr[i + k]
  
    # updates the max_sum
    if current_sum > max_sum:
        max_sum = current_sum

print(f"Maximum signal: {max_sum}")