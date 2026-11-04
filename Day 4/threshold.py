arr = list(map(int, input("Enter sensor flags: ").split()))
k = int(input("Enter window size: "))
t = int(input("Enter spike threshold: "))

curr = sum(arr[:k])
max_count = curr

for i in range(len(arr) - k):
    curr = curr - arr[i] + arr[i + k]
    if curr > max_count:
        max_count = curr

if max_count >= t:
    print(f"Alert: YES ({max_count} spikes)")
else:
    print(f"Alert: NO ({max_count} spikes)")

