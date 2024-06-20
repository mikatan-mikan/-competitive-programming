n = int(input())

a = list(map(int,input().split()))

t,s = [],[]

for i in range(n - 1):
    s_,t_ = map(int,input().split())
    if a[i] >= s_:
        a[i + 1] += t_ * (a[i] // s_)
        a[i] = a[i] % s_

print(a[-1])

