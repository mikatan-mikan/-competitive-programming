n,m = map(int,input().split())

s = input()
t = input()
x = ["#" for _ in range(n)]

tpl = 0

do = set()#既に試した場所
isb = False

#実際に前から試せばよい
now_char_pl = 0
while True:
    move = 0
    #現在地からどこまで一致しているか
    for i in range(m):
        if i + now_char_pl >= n:
            isb = True
            break
        #文字が一致している又は破棄してよい文字なら
        if s[i + now_char_pl] == t[i] or x[i + now_char_pl] != "#":
            tpl += 1
        else:
            break

print("Yes")