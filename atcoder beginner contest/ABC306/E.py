n,k,q = map(int,input().split())

now_a = [0 for _ in range(n)]

max = [[0,0],[0,0]]

for i in range(q):
    x,y = map(int,input().split())
    if y > max[1][0]:
        if y > max[0][0]:
            max[0][0] = y
            max[0][1] = 1 #出現回数
        else:
            max[1][0] = y
            max[1][1] = 1 #出現回数
    if now_a[x - 1] > y:
        if max[0][0] == now_a[x - 1]:
            max[0][1] -= 1
            if 
        if max[1][0] == now_a[x - 1]:
            max[1][1] -= 1
    now_a[x - 1] = y