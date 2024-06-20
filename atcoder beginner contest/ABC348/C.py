n = int(input())

exist_color = set()
color_beans = dict()
min_list = dict()

from collections import deque

for i in range(n):
    a,c = map(int,input().split())
    if c in exist_color:
        color_beans[c].append(a)
        min_list[c] = min(min_list[c],a)
    else:
        exist_color.add(c)
        color_beans[c] = deque([a])
        min_list[c] = a

max_ = -1

for color in min_list:
    if max_ < min_list[color]:
        max_ = min_list[color]

print(max_)