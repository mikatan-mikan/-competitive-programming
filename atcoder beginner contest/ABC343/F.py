class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        self.build(arr, 1, 0, self.n - 1)

    def build(self, arr, node, start, end):
        if start == end:
            self.tree[node] = [arr[start]]
            return
        mid = (start + end) // 2
        self.build(arr, 2 * node, start, mid)
        self.build(arr, 2 * node + 1, mid + 1, end)
        self.tree[node] = sorted(self.tree[2 * node] + self.tree[2 * node + 1])

    def update(self, node, start, end, idx, val):
        if start == end:
            self.tree[node] = [val]
            return
        mid = (start + end) // 2
        if start <= idx <= mid:
            self.update(2 * node, start, mid, idx, val)
        else:
            self.update(2 * node + 1, mid + 1, end, idx, val)
        self.tree[node] = sorted(self.tree[2 * node] + self.tree[2 * node + 1])

    def query(self, node, start, end, left, right, k):
        if left > end or right < start:
            return 0
        if left <= start and end <= right:
            return self.count_second_largest(self.tree[node], k)
        mid = (start + end) // 2
        return self.query(2 * node, start, mid, left, right, k) + \
               self.query(2 * node + 1, mid + 1, end, left, right, k)

    def count_second_largest(self, arr, k):
        count = 0
        for num in arr:
            if num != arr[-1] and num != arr[-2]:
                count += 1
        return count

N, Q = map(int, input().split())
A = list(map(int, input().split()))

seg_tree = SegmentTree(A)

for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        seg_tree.update(1, 0, N - 1, query[1] - 1, query[2])
    elif query[0] == 2:
        print(seg_tree.query(1, 0, N - 1, query[1] - 1, query[2] - 1, 2))