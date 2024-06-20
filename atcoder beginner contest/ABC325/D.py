n = int(input())

time = [list(map(int,input().split())) for _ in range(n)]


# time[i][0]を昇順に、time[i][0]が同じ場合はtime[i][1]を降順にソート
sorted_time = sorted(time, key=lambda x: (x[0], x[1]))
cnt = 0

from collections import deque


class add_sort_deque(deque):
    def append(self, x:list):
        #二分探索を用いてx[0] + x[1]を適切な場所に挿入する
        left = 0
        right = len(self)
        while left < right:
            mid = (left + right) // 2
            tmp = self[mid]
            if tmp[0] + tmp[1] < x[0] + x[1]:
                left = mid + 1
            else:
                right = mid
        self.insert(left, x)

que = add_sort_deque()
#n個のデータを前から処理する
for i in range(n):
    que.append(sorted_time[i])
    if i < n - 1:
        if sorted_time[i][0] == sorted_time[i + 1][0]:#次のも同じ時間ならqueに突っ込む
            continue
        else:
            next_time = sorted_time[i + 1][0] - sorted_time[i][0]#繰り返し猶予 
    else:
        next_time = 10**18
    choice_time = sorted_time[i][0]#現在の時刻
    while (next_time > 0) and que:#繰り返し猶予
        out = que.popleft()
        if out[0] + out[1] < choice_time:#廃棄
            continue
        next_time -= 1
        choice_time += 1
        cnt += 1


print(cnt)