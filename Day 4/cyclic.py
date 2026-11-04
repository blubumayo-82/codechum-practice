s = input("Enter a string: ")

current = s
smallest = s

for i in range(len(s)):
    current = current[1:] + current[0]
    if current < smallest:
        smallest = current

print(f"Smallest shift: {smallest}")