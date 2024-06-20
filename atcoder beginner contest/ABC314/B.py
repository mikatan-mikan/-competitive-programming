n = int(input())

c = []
a = []

for i in range(n):
    c.append(int(input()))
    a.append(set(map(int,input().split())))

x = int(input())
min_ = float('inf')
ans = []

for i in range(len(a)):
    if x in a[i]:
        if min_ == len(a[i]):
            ans.append(i + 1)
        elif min_ > len(a[i]):
            min_ = len(a[i])
            ans.clear()
            ans.append(i + 1)

print(len(ans))
print(*ans)