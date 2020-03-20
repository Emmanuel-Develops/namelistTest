a = int(input("Enter dividend: "))
b = int(input("Enter divisor: "))
c = a
d = 0

while a >= b:
    a = a - b
    d += 1
    if a < b:
        break
print('{} divided by {} is {} and remainder is {}'.format(c, b, d, a))

