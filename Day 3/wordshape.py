s = input("Enter a string: ")
upper = 0
lower = 0
digit = 0
symbol = 0

for ch in s:
    if ch.isdigit():
        digit += 1
    elif ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1
    else:
        symbol += 1

print(f"Uppercase letters: {upper}")
print(f"Lowercase letters: {lower}")
print(f"Digits: {digit}")
print(f"Symbols: {symbol}")