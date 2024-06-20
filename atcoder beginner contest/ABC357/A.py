n,h = map(int,input().split())

h_ = list(map(int,input().split()))

ans = 0

for i in range(n):
    if h_[i] <= h:
        h -= h_[i]
        ans += 1
    else:
        break

print(ans) 