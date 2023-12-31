#ズレの絶対値がkより大きければ、一致できない
n,k = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

dn = 0

for a_,b_ in zip(a,b):
    dn += abs(a_ - b_)

if dn > k:
    print("No")
    exit()
k -= dn
if k % 2 == 0:
    print("Yes")
else:
    print("No")