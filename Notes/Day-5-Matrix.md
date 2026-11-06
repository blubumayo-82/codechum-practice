## Core Matrix Cheatsheet & Patterns

### A. Coordinate System
```text
matrix[row_index][column_index]
r: 0 to R - 1 (vertical: top to bottom)
c: 0 to C - 1 (horizontal: left to right)
```

### B. Standard Ingestion
```python
# Reading dimensions and space-separated lines
R, C = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(R)]
```

### C. Creating an Empty $R \times C$ Grid
```python
# Always use list comprehension to avoid linked row references
grid = [[0] * C for _ in range(R)]
```

### D. Diagonals (Square $N \times N$)
* **Main Diagonal (top-left to bottom-right):**
  $$\text{cell } = (i, i) \implies \text{grid}[i][i]$$
* **Anti-Diagonal (top-right to bottom-left):**
  $$\text{cell } = (i, N - 1 - i) \implies \text{grid}[i][N - 1 - i]$$

### E. Border Traversal
```python
for r in range(M):
    for c in range(N):
        if r == 0 or r == M - 1 or c == 0 or c == N - 1:
            # cell (r, c) is on the boundary
            pass
```

### F. Column Operations: Extract $\rightarrow$ Sort $\rightarrow$ Overwrite
Because Python stores matrices row-by-row, columns must be gathered across rows:

```python
for c in range(C):
    # 1. Extract vertical column into a flat list
    col = [matrix[r][c] for r in range(R)]
    
    # 2. Sort the column values
    col.sort()
    
    # 3. Overwrite the original matrix column in-place
    for r in range(R):
        matrix[r][c] = col[r]
```

### G. Clean Matrix Output
```python
for row in matrix:
    print(*row)  # Unpacks list elements separated by single spaces
```

---

## Key Lessons Learned Tonight

1. **Parity Checks:**
   * Odd: `N % 2 != 0` (or `N % 2 == 1`)
   * Even: `N % 2 == 0`
   * *(Note: `N % 1` is always 0 for any integer).*

2. **Loop Boundaries:**
   * `range(N)` runs indices $0, 1, \dots, N - 1$ ($N$ elements total).
   * `range(N - 1)` drops the last element ($N - 2$).

3. **Loop Indentation (Early Returns):**
   * Keep `return True` outside the divisor checking loop when validating primes, or the function will return on the very first check.

4. **CodeChum Formatting Guardrails:**
   * Match spaces inside prompts verbatim: `"Enter number of rows (M): "` vs `"Enter number of rows(M): "`.
   * Watch for unwanted trailing whitespace in `print()` statements.