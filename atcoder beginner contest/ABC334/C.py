#貪欲でよさそう？
n,k = map(int,input().split())

from sortedcontainers import SortedList

a :list[int] = SortedList(map(int,input().split()))
ans = 0

#kが奇数の場合
if k % 2 == 1:
    #累積和
    sum_a = [0 for _ in range(k//2)]
    sum_a_ = [0 for _ in range(k//2)]
    for i in range(1,k + 1,2):
        if i <= k - 1:
            sum_a[i // 2] = sum_a[i // 2 - 1] + (a[i] - a[i - 1])
        if i <= k - 2:
            sum_a_[i // 2] = sum_a_[i // 2 - 1] + (a[i + 1] - a[i])

    now_choose = 10**18

    #iまでの範囲のコストとi以降から最後を除く範囲、iまでのコストとi + 1以降。
    #この二つのコストの和が最大になる場所でiを選ぶ
    for i in range(0, k//2):
        now = sum_a[i] + (sum_a_[-1] - sum_a_[i])#現在のコスト
        if now < now_choose:
            now_choose = now
            ans = i * 2 + 1
    print(now_choose if now_choose != 10**18 else 0)
else:
    for i in range(1,n + 1):
        if len(a) == 0:
            break
        if a[0] == i:
            if len(a) >= 2:
                ans += abs(a[0] - a[1])
                a.pop(0)
                a.pop(0)

    print(ans)