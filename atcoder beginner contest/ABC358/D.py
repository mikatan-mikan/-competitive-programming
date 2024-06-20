n,m = map(int,input().split())

a = list(map(int,input().split()))
b = list(map(int,input().split()))

a.sort()
b.sort()

a_ptr = 0

ans = 0

for i in range(m):
    want = b[i]
    while True:
        if a_ptr >= n:
            print(-1)
            exit()
        if a[a_ptr] >= want:#渡したい数より多いなら
            ans += a[a_ptr]
            a_ptr += 1
            break
        else:
            a_ptr += 1

print(ans)