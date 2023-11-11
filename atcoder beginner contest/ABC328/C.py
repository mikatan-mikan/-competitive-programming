n,q = map(int,input().split())

s = input()

#隣り合っている文字の累積和
sum_each = [0] * (n + 1)
for i in range(1,n):
    if s[i] == s[i - 1]:
        sum_each[i] = sum_each[i - 1] + 1
    else:
        sum_each[i] = sum_each[i - 1]


for i in range(q):
    l,r = map(int,input().split())
    #その区間における隣り合った文字の数
    print(sum_each[r - 1] - sum_each[l - 1])
