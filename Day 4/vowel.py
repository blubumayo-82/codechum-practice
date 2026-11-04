s = input("Enter text: ")
k = int(input("Enter window size: "))
vowel = ['a', 'e', 'i', 'o', 'u']

curr_vowels = 0
curr_vowels = 0
for ch in s[:k]:
    if ch in vowel:
        curr_vowels += 1

max_vowels = curr_vowels

for i in range(len(s) - k):
    if s[i] in vowel:
        curr_vowels -= 1
    if s[i+k] in vowel:
        curr_vowels += 1
    if curr_vowels > max_vowels:
        max_vowels = curr_vowels

print(f"Maximum vowels: {max_vowels}")
        
