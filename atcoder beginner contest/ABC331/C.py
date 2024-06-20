n = int(input())
a:list[int] = list(map(int,input().split()))
a_c = a.copy()
a.sort()
a_d = {a[i]:i for i in range(n)}

#累積和
sum_ = [0 for i in range(n)]
sum_[0] = a[0]
for i in range(1,n):
    sum_[i] = a[i] + sum_[i-1]

for i in range(n):
    print(sum_[-1] - sum_[a_d[a_c[i]]],end=" ")

