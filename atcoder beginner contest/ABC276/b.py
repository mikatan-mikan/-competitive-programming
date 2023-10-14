from collections import deque

N , M = map(int,input().split())

path = deque()

path = [deque(map(int,input().split())) for _ in range(M)]

# for i in range(M):
#     path.append(deque(map(int,input().split())))

out = deque([deque() for _ in range(N)])#aiからbjにわたる際(ai,bj)があったならi番目にbjをj番目にaiを
pop = deque()
path = sorted(path)#1からつながるのは前の方に集まる
# print(path)

for i in path:#m本の道を見る
    out[i[0] - 1].append(i[1])
    out[i[1] - 1].append(i[0])

for i in out:
    print(len(i),*i)