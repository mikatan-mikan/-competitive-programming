l,r = map(int,input().split())

now_l = l

box = 2#広さ

from collections import deque

ans = deque()

#広げる
while True:
    if now_l % box != 0:#割り切れなければ(きれいな場所でなければ)
        ans.append([now_l,now_l + (box // 2)])
        now_l += box // 2
    if now_l + box <= r:
        box += box
    else:
        break

ans_2 = deque()

box = 2 ** 61

#狭める
while True:
    if now_l + box <= r:#割り切れなければ(きれいな場所でなければ)
        ans.append([now_l,now_l + (box)])
        now_l += box
    box //= 2
    if now_l == r:
        break
    
    if box == 0:
        raise ValueError

print(len(ans))

for i in range(len(ans)):
    print(*ans[i])