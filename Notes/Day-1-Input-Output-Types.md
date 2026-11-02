# NPC Day 1 - I/O and Types Cheat Sheet

### Single Values

```python
# Text
name = input()

# Whole numbers
n = int(input())

# Decimals
val = float(input())
```

### Multiple Values on a Single Line

```python
# Fixed number of variables (space-separated)
a, b = map(int, input().split())
code, price, qty = input().split()
price = float(price)
qty = int(qty)

# Variable-length list of integers
nums = list(map(int, input().split()))
```

### Multiple Lines with a Given Count ($N$)

```python
# Reading N numbers into a list
n = int(input())
lines = [int(input()) for _ in range(n)]

# Processing N items directly in a loop
n = int(input())
for _ in range(n):
    name, score = input().split()
    score = float(score)
    # Process immediately
```

### Reading a 2D Matrix ($R$ rows, $C$ columns)

```python
# Read dimensions then rows
r, c = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(r)]
```

### Unknown Number of Lines (Until EOF)

```python
import sys

# sys.stdin.read().splitlines() grabs every line until the end of input
lines = sys.stdin.read().splitlines()

for line in lines:
    if line:  # skip any accidental empty lines
        val = int(line)
        # process val
```

### Output Formatting & Printing

```python
# Format float to 2 decimal places:
print(f"{val:.2f}")

# Format with leading zeros (2 digits wide):
hours = 9
mins = 5
print(f"{hours:02d}:{mins:02d}")  # Outputs: 09:05

# Print space-separated list without brackets:
print(*nums)  # or: print(" ".join(map(str, nums)))

# Custom separator between values:
# Prints: 2026-11-14
print("2026", "11", "14", sep="-")

# Prevent automatic newline:
print("Hello", end=" ")
```

### High-Frequency Trap Avoidance

```python
# 1. Use input().split() with no arguments (cleanly handles extra/irregular spaces)
# 2. Never use round(x, 2) for output; use f"{x:.2f}" to keep trailing zeros
# 3. Clean clamping in one line:
boosted = min(100, score + 5)
```