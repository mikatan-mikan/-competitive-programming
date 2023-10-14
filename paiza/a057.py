n = int(input())
s = [input() for _ in range(n)]

move = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]

max_ = 0

for mode in [1,-1]:#加算ver or 減算ver
    for i in range(n):
        for j in range(n):#全てのマスに対して
            for go in range(len(move)):
                first_place = int(s[i][j])#これから減算加算が続いている数を調べる
                cnt = 1
                leng = 0
                while True:
                    leng += 1
                    if i + move[go][0] * leng < 0 or i + move[go][0] * leng >= n or j + move[go][1] * leng < 0 or j + move[go][1] * leng >= n:
                        break
                    if int(s[i + move[go][0] * leng][j + move[go][1] * leng]) == first_place + leng * mode:
                        cnt += 1
                        if cnt > max_:
                            max_ = cnt
                    else:
                        break


print(max_)



