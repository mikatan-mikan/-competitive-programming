a = []

while True:
    a.append(int(input()))
    if a[-1] == 0:
        break

a.reverse()

for i in a:
    print(i)