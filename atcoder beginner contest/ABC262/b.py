
N , M = map(int,input().split())

U_V = set()
for i in range(M): 
    U_V.add(tuple(map(int,input().split())))


print(U_V)
cnt = 0


for a in range(1,N + 1):
    for b in range(a + 1,N + 1):
        for c in range(b + 1,N + 1):
            if ((a,b) in U_V):
                if ((b,c) in U_V):
                    if ((a,c) in U_V):
                        cnt +=1

print(cnt)