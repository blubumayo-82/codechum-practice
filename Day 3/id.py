s = input("Enter studnt ID code: ")

if len(s) < 5:
    print("Error: Code too short")
else:
    if s[0].isupper() and s[1].isupper():
        print("Status: Department Admin Code")
    elif s[0].isupper() and s[1].isdigit():
        print("Status: Student Standard ID")
    else:
            print("Status: General Guest Pass")