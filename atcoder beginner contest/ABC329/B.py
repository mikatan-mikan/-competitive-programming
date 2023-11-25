n = int(input())

a = list(map(int,input().split()))

a.sort(reverse=True)

r = a[0]

while True:
    if a[0] == r:
        del a[0]
    else:
        break

print(a[0])