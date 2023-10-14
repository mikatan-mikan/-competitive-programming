s = list(map(int,input().split()))

bef = 0

for i in s:
    if i < 100 or i > 675:
        print("No")
        exit()
    if i % 25 != 0:
        print("No")
        exit()
    if i < bef:
        print("No")
        exit()
    bef = i
print("Yes")