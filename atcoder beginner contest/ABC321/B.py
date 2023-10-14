n,x = map(int,input().split())
a = list(map(int,input().split()))
a.sort()
min_ = a[0]
max_ = a[-1]
sum_ = sum(a[1:-1])

#既に点が足りているなら必要なのは0
if sum_ + min_ >= x:
    print(0)
else:#点が足りずminを加算しても足りない場合
    ans = x - sum_
    if ans > max_:
        print(-1)
        exit()
    print(ans if ans <= 100 else -1)
