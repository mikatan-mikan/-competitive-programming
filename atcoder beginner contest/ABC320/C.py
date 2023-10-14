import sys
sys.setrecursionlimit(10**9)

m = int(input())

s = [input() for _ in range(3)]

#sの中身をそれぞれ3回繰り返す
s[0] = s[0] + s[0] + s[0]
s[1] = s[1] + s[1] + s[1]
s[2] = s[2] + s[2] + s[2]

number = 0
minimum = 10 ** 9

def dfs(now_not_pressed:set,press_place):#numberをまだpressされていない位置から探してpressする
    #未探索が空なら
    if len(now_not_pressed) == 0:
        global minimum
        minimum = min(minimum,max(press_place))
        return
    global number
    for next in now_not_pressed:
        for i in range(m * 3):
            if s[next][i] == str(number) and i not in press_place:
                press_place[next] = i
                arg = now_not_pressed.copy()
                arg.remove(next)
                dfs(arg,press_place)


for i in range(10):
    number = i
    dfs(set([0,1,2]),[101,101,101])

print(minimum if minimum != 10 ** 9 else -1)