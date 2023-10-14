n = int(input())
a = list(map(int,input().split()))

bef = a[0]

for num in a:
    if bef != num:
        print("No")
        exit()
    bef = num

print("Yes")