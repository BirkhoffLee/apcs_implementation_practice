numbers = [ int(k) for k in input().split() ]
numbers.sort()

a, b, c = numbers[0], numbers[1], numbers[2]

cc = c * c
check = a * a + b * b

print("{} {} {}".format(a, b, c))

if a + b <= c:
    print("No")
elif check < cc:
    print("Obtuse")
elif check == cc:
    print("Right")
elif check > cc:
    print("Acute")
else:
    print("wtf")
