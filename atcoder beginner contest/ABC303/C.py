N,M,H,K = map(int,input().split())
S = input()
place = set()

for _ in range(M):
    place.add(tuple(map(int,input().split())))

player = [0,0] # x,y

for Next in S:
    if Next == 'R':
        player[0] += 1
    elif Next == 'L':
        player[0] -= 1
    elif Next == 'U':
        player[1] += 1
    elif Next == 'D':
        player[1] -= 1
    H -= 1
    if H < 0:
        print('No')
        exit()
    if tuple(player) in place:
        if H < K:
            H = K
            place.remove(tuple(player))

print('Yes')