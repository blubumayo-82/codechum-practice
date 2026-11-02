n = int(input())
lines = [int(input()) for _ in range(n)]

dep = 0
wt = 0
bal = 0
for i in lines:
    if i > 0:
        dep += i
        bal += i
    elif i < 0:
        wt += abs(i)
        bal += i
        
print(f"Deposits: {dep}")
print(f"Withdrawals: {wt}")
print(f"Final Balance: {bal}")