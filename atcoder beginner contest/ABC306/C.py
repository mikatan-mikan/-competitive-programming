from collections import deque

N = int(input())

A = list(map(int,input().split()))

visited = set() #既に存在したか
visited_2nd = set() #既に2回以上存在したか
ans = deque()

for i in A:
    if i not in visited_2nd:
        if i in visited:
            ans.append(i)
            visited_2nd.add(i)
        else:
            visited.add(i)

print(*ans)