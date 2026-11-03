# NPC Day 2 - Conditionals, Floating-Point Traps & Branching Mastery

### 1. Multi-Branch Conditionals & Chained Comparisons

```python
# Standard 3-way comparison with tie-breaker
if val_a > val_b:
    print("A wins")
elif val_b > val_a:
    print("B wins")
else:
    print("Tie")

# Pythonic Chained Comparisons (Inclusive & Exclusive Ranges)
if 18.5 <= bmi < 25.0:
    print("Normal")

# Ternary One-Liner (Quick assignment based on condition)
status = "Valid" if checksum % key == 0 else "Corrupt"
```

### 2. Relative Percentage & Rate Comparison Formulas

```python
# Relative Percentage Difference (How much higher winner is vs loser):
# ALWAYS divide by the reference/smaller baseline value when asked "more efficient by X%"
diff_pct = ((higher - lower) / lower) * 100
print(f"Car A is more efficient by {diff_pct:.2f}%")

# Percentage Change (From Old to New):
pct_change = ((new_val - old_val) / old_val) * 100
```

### 3. Floating-Point Precision Trap (`math.isclose` & Cross-Multiplication)

```python
# TRAP: 0.1 + 0.2 == 0.3 evaluates to False in Python (0.30000000000000004)!
# Fix 1: Epsilon tolerance check for float equality
if abs(eff_a - eff_b) < 1e-9:
    print("Both cars have the same efficiency")

# Fix 2: Cross-Multiplication (Avoids float division completely when inputs are ints/exact)
# Instead of (d / a) > (d / b), compare (d * b) > (d * a)
```

### 4. Tiered Bracket / Progressive Tax Logic

```python
# Computing progressive tiers (e.g., electric bills, tax brackets, shipping rates)
# First 100 units at $5, next 100 at $8, anything above 200 at $12:
if units <= 100:
    cost = units * 5
elif units <= 200:
    cost = (100 * 5) + ((units - 100) * 8)
else:
    cost = (100 * 5) + (100 * 8) + ((units - 200) * 12)
```

### 5. Divisibility & Zero-Division Guards

```python
# Always guard against ZeroDivisionError using short-circuit evaluation:
if b != 0 and a % b == 0:
    print("Divisible")

# Leap Year Classic Rule (Divisible by 4, EXCEPT century years unless divisible by 400):
is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
```