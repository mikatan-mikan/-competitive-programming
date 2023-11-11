class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:
                root_x, root_y = root_y, root_x
            self.parent[root_y] = root_x
            if self.rank[root_x] == self.rank[root_y]:
                self.rank[root_x] += 1


def kruskal(graph, n, k):
    edges = sorted(graph, key=lambda x: x[2] % k)  # 余りでソート
    uf = UnionFind(n)
    min_cost = 0

    for edge in edges:
        u, v, w = edge
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            min_cost += w

    return min_cost % k


# 入力の処理
N, M, K = map(int, input().split())
graph = []
for i in range(M):
    u, v, w = map(int, input().split())
    graph.append((u - 1, v - 1, w))

# kで割った余りが最小の最小全域木のコストを計算
result = kruskal(graph, N, K)
print(result)