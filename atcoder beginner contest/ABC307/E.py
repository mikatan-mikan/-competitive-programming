n,m = map(int,input().split())

ans = [0] * n
ans[0] = m

for i in range(1,n - 1):
    ans[i] = (ans[i - 1] * (m - 1)) % (998244353)

print((ans[-2] * ((m - 2) if m > 2 else 1)) % (998244353))