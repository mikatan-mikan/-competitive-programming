h,w = map(int,input().split())

s = [list(input()) for _ in range(h)]

mag = set()#磁石の影響を受けるもの

for y in range(0,h):
    for x in range(0,w):
        if s[y][x] == "#":
            continue
        for dy,dx in [(1,0),(0,1),(-1,0),(0,-1)]:
            if 0 <= y + dy < h and 0 <= x + dx < w:
                if s[y + dy][x + dx] == "#":
                    s[y][x] = "*"
                    mag.add(y + x * 1000)
                    break

visited = set()
ans_max = 1#磁石のみの1(じしゃくが0ならそれはそれで1以上のはず)

from collections import deque

non = set(["#","*"])
go = set([".","*"])

#(y,x)が初期の座標
for y in range(h):
    for x in range(w):
        #探索済みならそこから出ても結果は変わらないのでスキップ
        if y + x * 1000 in visited or s[y][x] in non:
            continue
        #そうでないならそこからbfsする
        can_go = 0
        visited.add(y + x * 1000)
        mag_visited = set()
        que = deque([(y,x)])
        while que:
            y_,x_ = map(int,que.popleft())
            can_go += 1
            #もし磁石に阻まれていたなら探索を打ち切る
            if s[y_][x_] == "*":
                continue
            #そうでなければ次の場所を入れる。
            for dy,dx in [(1,0),(0,1),(-1,0),(0,-1)]:
                if 0 <= y_ + dy < h and 0 <= x_ + dx < w:
                    if s[y_ + dy][x_ + dx] in go and (y_ + dy) + (x_ + dx)*1000 not in visited and (y_ + dy) + (x_ + dx)*1000 not in mag_visited:
                        que.append((y_ + dy, x_ + dx))
                        if s[y_ + dy][x_ + dx] != "*":
                            visited.add((y_ + dy) + (x_ + dx)*1000)
                        else:
                            mag_visited.add((y_ + dy) + (x_ + dx)*1000)
        ans_max = max(ans_max,can_go)


print(ans_max)