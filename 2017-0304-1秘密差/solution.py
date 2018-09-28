num = input()
odd = 0
even = 0
for i, char in enumerate(num):
    if i % 2 == 0:
        # even
        even += int(char)
    else:
        odd += int(char)
print(abs(odd-even))