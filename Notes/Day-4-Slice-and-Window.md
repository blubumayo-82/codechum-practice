# Competitive Programming Notes: Day 4
## String Slicing, Circular Buffers & Sliding Window Techniques

---

## 1. Slicing & Cyclic String Rotations

### Basic Slicing Review
In Python, slicing follows `sequence[start:stop:step]`, where `stop` is non-inclusive.

* **Left Rotation by 1:** Shift everything to the left; the first character moves to the very back.
  ```python
  rotated_left = s[1:] + s[0]
  ```
* **Right Rotation by 1:** Shift everything to the right; the last character moves to the very front.
  ```python
  rotated_right = s[-1] + s[:-1]
  ```

---

## 2. The "Double Structure" Trick (`s + s` / `arr + arr`)

When handling circular arrays, ring buffers, or cyclic rotations, wrap-around conditions can create messy index math or boundary bugs. 

### The Solution:
Duplicate the array or string:
```python
double_s = s + s
double_arr = arr + arr
```

### Why it works:
* Every possible cyclic shift or wrap-around contiguous subsegment of length $N$ exists as a simple linear slice inside the doubled structure.
* Window $i$ in a ring of size $N$ starts at index `i` and spans `double_arr[i : i + k]`.
* Eliminates modulo arithmetic (`%`) and negative index lookups.

---

## 3. Fixed-Size Sliding Window Fundamentals

### The Philosophy: Reusing Work
Instead of recalculating an entire window from scratch ($O(N \times K)$ brute force), maintain a running sum/state and update it in $O(1)$ constant time as the window shifts.

$$\text{new\_state} = \text{old\_state} - \text{element leaving left} + \text{element entering right}$$

### The Boundary Math (The "Why")

1. **`len(arr) - k + 1` (Total Windows):**
   * The total count of valid contiguous subarrays of length $k$.
   * A window cannot start past `len(arr) - k` because there would not be enough elements remaining to complete a window of size $k$.

2. **`len(arr) - k` (Remaining Slides):**
   * Used in sliding window loops when the first window (`arr[:k]`) is pre-computed *before* the loop.
   * Total windows = `len(arr) - k + 1`.
   * Pre-computed windows = `1`.
   * Remaining slides = `(len(arr) - k + 1) - 1` = `len(arr) - k`.

3. **`range(n - 1)` (Doubled Circular Arrays):**
   * In an array of size $N$, there are exactly $N$ circular windows.
   * Solving the first window leaves exactly $N - 1$ slides to evaluate all circular positions.

---

## 4. Standard Code Templates

### Template A: Fixed-Size Numeric Extremum (Max / Min)
```python
arr = list(map(int, input("Enter values: ").split()))
k = int(input("Enter window size: "))

# 1. Compute the first window
curr = sum(arr[:k])
best = curr

# 2. Slide across the remaining elements
for i in range(len(arr) - k):
    curr = curr - arr[i] + arr[i + k]
    if curr > best:  # or curr < best for minimum
        best = curr

print(f"Result: {best}")
```

### Template B: Character / Condition-Based Tracking
When tracking conditions (like vowels or flags), treat matching elements as `+1` and non-matching elements as `0`.

```python
s = input("Enter text: ")
k = int(input("Enter window size: "))
vowels = {'a', 'e', 'i', 'o', 'u'}

# 1. Count vowels in the initial window
curr_vowels = sum(1 for ch in s[:k] if ch in vowels)
max_vowels = curr_vowels

# 2. Slide and update condition
for i in range(len(s) - k):
    if s[i] in vowels:
        curr_vowels -= 1
    if s[i + k] in vowels:
        curr_vowels += 1
    if curr_vowels > max_vowels:
        max_vowels = curr_vowels

print(f"Maximum vowels: {max_vowels}")
```

### Template C: Circular Buffer Window
```python
arr = list(map(int, input("Enter values: ").split()))
k = int(input("Enter window size: "))

n = len(arr)
double_arr = arr + arr

curr = sum(double_arr[:k])
max_val = curr

# Exactly n - 1 slides check all n circular windows
for i in range(n - 1):
    curr = curr - double_arr[i] + double_arr[i + k]
    if curr > max_val:
        max_val = curr

print(f"Maximum: {max_val}")
```

---

## 5. Preview: Dynamic (Variable-Size) Sliding Windows

For problems where window size $K$ is **not fixed**, use the two-pointer technique (`left` and `right`):

* **Expand (`right += 1`):** Add incoming elements to satisfy or test a condition.
* **Shrink (`left += 1`):** Remove outgoing elements while the condition is violated or when minimizing the window length.
* **Length Formula:** $\text{Window Length} = \text{right} - \text{left} + 1$.
* **Time Complexity:** $O(N)$ linear time, because both `left` and `right` only traverse the array once from left to right.