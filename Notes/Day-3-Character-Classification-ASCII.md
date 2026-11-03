# NPC Day 3 - Character Classification & ASCII Cheat Sheet

### Built-in Character Classification Methods

```python
s = input("Enter a string: ")

upper = 0
lower = 0
digits = 0
symbols = 0

for ch in s:
    if ch.isupper():        # Checks 'A' through 'Z'
        upper += 1
    elif ch.islower():      # Checks 'a' through 'z'
        lower += 1
    elif ch.isdigit():      # Checks '0' through '9'
        digits += 1
    else:                   # Spaces, punctuation, special chars
        symbols += 1
```

### Direct ASCII Value Conversion (`ord` and `chr`)

```python
# Get integer ASCII value of a single character:
val = ord('A')   # 65
val = ord('a')   # 97
val = ord('0')   # 48

# Convert integer ASCII value back to a character:
ch = chr(65)     # 'A'

# Zero-based alphabet index (0 to 25):
idx = ord(ch) - ord('A')
```

### Common Character Checks

```python
ch.isalpha()     # True if uppercase OR lowercase letter
ch.isalnum()     # True if letter OR digit (False for spaces/symbols)
ch.isspace()     # True if space, tab, or newline
```