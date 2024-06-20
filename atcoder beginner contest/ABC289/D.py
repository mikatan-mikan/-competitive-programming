import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)
N = int(input())
A = list(map(int,input().split()))
M = int(input())
B = set(map(int,input().split()))
X = int(input())

visited = set()##既に行った場所に行っても仕方がないので

def dfs(place):
    global A,B
    for i in A:
        if place + i not in B and place + i <= X and place + i not in visited:
            if place + i == X:
                print("Yes")
                exit()
            visited.add(place + i)
            dfs(place + i)

##dfsしてみる
dfs(0)
print("No")