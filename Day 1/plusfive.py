nums = list(map(int, input().split()))
maxed = 0
for i in range(len(nums)):
    nums[i] += 5

for n in range(len(nums)):
    if nums[n] > 100:
        s = nums[n] - 100
        nums[n] -= s
        maxed += 1
    else:
        continue

print(*nums)
print(f"Maxed: {maxed}")