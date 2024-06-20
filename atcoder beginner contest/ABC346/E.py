h,w,m = map(int,input().split())

from sortedcontainers import SortedList


#[時刻:色]
#最終的に時刻が大きいものから処理していく(その際、それまでに何列何行出力したかを覚えて、減算処理をする)
h_color = list([2*10**6,0] for _ in range(h))
w_color = list([2*10**6,0] for _ in range(w))

for i in range(m):
    t,a,x = map(int,input().split())
    if t == 1:
        h_color[a - 1] = [(2*10**6) - (i + 1),x]
    else:
        w_color[a - 1] = [(2*10**6) - (i + 1),x]

h_color = SortedList(h_color)
w_color = SortedList(w_color)

#小さいものから出力する
use_h,use_w = 0,0
ans = {}
while True:
    if h_color[0][0] > w_color[0][0]:
        if w_color[0][1] in ans:
            ans[w_color[0][1]] += h - use_h
        else:
            ans[w_color[0][1]] = h - use_h
        use_w += 1
        #先頭を削除
        w_color.pop(0)
        
    else:
        if h_color[0][1] in ans:
            ans[h_color[0][1]] += w - use_w
        else:
            ans[h_color[0][1]] = w - use_w
        use_h += 1
        #先頭を削除
        h_color.pop(0)
    if len(h_color) == 0 or len(w_color) == 0:
        break

if len(h_color) == 0:
    while True:
        if w_color[0][1] in ans:
            ans[w_color[0][1]] += h - use_h
        else:
            ans[w_color[0][1]] = h - use_h
        use_w += 1
        #先頭を削除
        w_color.pop(0)
        if len(w_color) == 0:
            break
elif len(w_color) == 0:
    while True:
        if h_color[0][1] in ans:
            ans[h_color[0][1]] += w - use_w
        else:
            ans[h_color[0][1]] = w - use_w
        use_h += 1
        #先頭を削除
        h_color.pop(0)
        if len(h_color) == 0:
            break


ans_list = sorted([[key, ans[key]] for key in ans if ans[key] != 0])

print(len(ans_list))

for i in range(len(ans_list)):
    print(ans_list[i][0],ans_list[i][1])