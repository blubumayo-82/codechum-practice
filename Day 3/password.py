s = input("Enter a password: ")
uppercase = 0
lowercase = 0
digit = 0
symbol = 0


for ch in s:
    if ch.isdigit():  
        digit += 1
    elif ch.isupper():
        uppercase += 1
    elif ch.islower():
        lowercase += 1
    else:
        symbol += 1

print(f"Uppercase: {uppercase}")
print(f"Lowercase: {lowercase}")
print(f"Digits: {digit}")
print(f"Symbols: {symbol}")
if len(s) < 8:
    print("Status: Weak")
else:
    print("Status: Strong")


