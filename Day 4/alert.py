arr = list(map(int, input("Enter CPU logs: ").split()))
d = int(input("Enter duration: "))
t = int(input("Enter threshold: "))

alerts = 0

curr = sum(arr[:d])
if curr >= t:
    alerts += 1

for i in range(len(arr) - d):
    curr = curr - arr[i] + arr[i + d]
    if curr >= t:
        alerts += 1

print(f"High traffic alerts: {alerts}")