from collections import deque

N , M = map(int,input().split())

U_V = deque()
for i in range(M): 
    U_V.append(list(map(int,input().split())))

cnt = 0


for a in range(1,N + 1):
    for b in range(1,N + 1):
        for c in range(1,N + 1):
            if ([a,b] in U_V) and ([b,c] in U_V) and ([a,c] in U_V ):
                cnt +=1

print(cnt)