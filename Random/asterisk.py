n = int(input())

# Row of width n
print("*" * n)

# Rows from width n-1 down to 1
for width in range(n - 1, 0, -1):
    if width == 1:
        print("*")
    else:
        # 2 characters are asterisks, the rest (width - 2) are spaces
        print("*" + (" " * (width - 2)) + "*")