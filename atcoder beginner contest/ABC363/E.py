import heapq
from collections import deque

h, w, y = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]

arounded = set()  # 既に沈んだ or 周りの敷地を記録
around = dict()
# 次に沈む場所を管理(そこまで時間を進める)
heap = []
# 外側を採取
for i in range(h):
    for j in range(w):
        if i == 0 or j == 0 or i == h - 1 or j == w - 1:
            pos = (a[i][j], i * w + j)
            if a[i][j] not in around:
                around[a[i][j]] = deque([i * w + j])
            else:
                around[a[i][j]].append(i * w + j)
            heapq.heappush(heap, pos)
            arounded.add(i * w + j)

# 現在の海面
now_sea = 0
# 残っている敷地
field = h * w

# 時間を進める
for year in range(y):
    now_sea += 1
    if len(heap) == 0:  # もう陸が無ければ
        print(field)
        continue
    if heap[0][0] > now_sea:  # まだ沈む箇所が出なければ
        print(field)
        continue
    
    # 沈む場所を探してその周辺を追加
    while len(heap) > 0 and heap[0][0] <= now_sea:
        now, place = heapq.heappop(heap)
        xi = place // w
        yi = place % w
        # 周囲を探す
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            x, y = xi + dx, yi + dy
            if 0 <= x < h and 0 <= y < w:
                pos = x * w + y
                if pos not in arounded:
                    heapq.heappush(heap, (a[x][y], pos))
                    arounded.add(pos)
        # 敷地を減らす
        field -= 1
    print(field)