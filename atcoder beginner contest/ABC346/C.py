n,k = map(int,input().split())

a = list(map(int,input().split()))

sum_ = (k * (k + 1)) // 2


a_used = set()
#aの中身を
for i in range(n):
    if a[i] not in a_used:
        a_used.add(a[i])
        if a[i] <= k:
            sum_ -= a[i]

print(sum_)