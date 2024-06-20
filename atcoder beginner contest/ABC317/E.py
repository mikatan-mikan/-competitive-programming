from collections import deque

def dfs(path):
    max_weights = {}  # 訪問した各ノードの最大重みを格納する辞書
    stack = deque([(1, True, 0, set())])  # 初期ノードから開始
    while stack:
        now, is_count, w, visited = stack.pop()
        visited.add(now)
        if now in max_weights and max_weights[now] >= w:
            continue  # 以前に訪問され、より低い重みであるノードをスキップ
        max_weights[now] = w  # 現在のノードの最大重みを更新
        for weight, next_node in path[now]:
            if next_node in visited:
                continue
            plus = weight if is_count else 0
            stack.append((next_node, not is_count, w + plus, visited.copy()))

    return max_weights[1]  # 開始ノード1の最大重みを返す

n = int(input())
path = [deque() for _ in range(n + 1)]

for i in range(1, n):
    d = list(map(int, input().split()))
    for j in range(1, len(d) + 1):
        path[i].append((d[j - 1], i + j))
        path[i + j].append((d[j - 1], i))

max_w = dfs(path)
print(max_w)