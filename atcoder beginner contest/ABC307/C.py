from collections import deque
import sys

input = sys.stdin.readline


h_a,w_a = map(int,input().split())
a = deque()
for i in range(h_a):
    a.append(input())
h_b,w_b = map(int,input().split())
b = deque()
for i in range(h_b):
    b.append(input())
h_x,w_x = map(int,input().split())
x = deque()
for i in range(h_x):
    x.append(input())

c = [["." for _ in range(30)] for _ in range(30)]

for pl in range(160000):#aの初期位置
    a_pl = pl // 400
    b_pl = pl % 400
    for i in range(100):#コピー
        div = i // 10
        mod = i % 10
        if mod % 10 < h_a and div < w_a:
            c[a_pl % 20 + mod][a_pl // 20 + div] = a[mod][div]
        if mod < h_b and div < w_b:
            if b[mod][div] == "#":
                c[b_pl % 20 + mod][b_pl // 20 + div] = b[mod][div]
    cnt = 0
    for i in range(h_x * w_x):
        if c[10 + i % h_x][10 + i // h_x] == x[i % h_x][i // h_x]:
            cnt += 1
    if cnt == h_x * w_x:
        print("Yes")
        exit()
    c = [["." for _ in range(30)] for _ in range(30)]

print("No")