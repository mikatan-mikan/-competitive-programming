d = int(input())

x = 1
y = 1

min_ = 10**13

while True:
    if abs(x ** 2 + y ** 2 - d) < min_:
        min_ = abs(x ** 2 + y ** 2 - d)
    if x ** 2 + y ** 2 > 10 ** 12:
        x = 0
        y += 1
    x += 1
    if y ** 2 > 10 ** 12:
        break

print(min_)