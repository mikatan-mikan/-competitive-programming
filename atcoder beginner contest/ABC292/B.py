N, Q = map(int,input().split())

mem = [0 for _ in range(N)]

for i in range(Q):
    x_num, x_mem = map(int,input().split())
    if x_num == 1:
        mem[x_mem-1] += 1
    elif x_num == 2:
        mem[x_mem-1] += 2
    else:
        if mem[x_mem - 1] >= 2:
            print("Yes")
        else:
            print("No")
