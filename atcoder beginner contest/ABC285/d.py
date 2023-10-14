import sys
from collections import deque

sys.setrecursionlimit(10 ** 9)
N = int(input())

root = {}#pathを保存する(aからbへ)

#aからbへのpathを保存する
for i in range(N):
    place,to = map(str,input().split())
    if f"{place}" not in root: root.setdefault(f"{place}",deque([to]))
    else: root[f"{place}"].append(to)

def dfs(acc,f):#pathを深さ優先探索する
    global re,root
    if acc in re: return#自身に既に来たことがあればカット
    re.add(acc)#自身を追加しておく
    if acc in root:
        for list_in in root[acc]:
            if list_in in re:#もし行く先が探索済みで、一回目でなければ
                print("No")
                exit()
            #来たことがないのであれば
            else:
                dfs(list_in,True)#奥に進む


re = set()#既に訪れた名前を保管しておく
for i in root:
    dfs(i,False)
print("Yes")