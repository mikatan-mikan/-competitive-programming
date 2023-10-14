a,b = map(int,input().split())

c = 0

if a / 4 >= 1 or b / 4 >= 1:
    c += 4

if (a % 4) / 2 >= 1 or (b % 4) / 2 >= 1:
    c += 2

if ((a % 4) % 2) >= 1 or ((b % 4) % 2) >= 1:
    c += 1
print(c)