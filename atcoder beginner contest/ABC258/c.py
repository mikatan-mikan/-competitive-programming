from collections import deque
N,Q = map(int,input().split())
S = input()
for i in range(Q):
    query_num,query_x = map(int,input().split())
    if query_num == 1:
        tmp = S[N - (query_x):]
        S = S[:N - (query_x)]
        S = tmp + S
        #print(S,S[N - (query_x):])
    elif query_num == 2:
        print(S[query_x - 1])
        #dsuccxulnl
        #
        #nldsuccxul

    #lnldsuccxu
    #xulnldsucc
    #uccxulnlds]




提出 #32934262

ソースコード 

Copy
Copy
import numpy as np
 
N = int(input())
A = []
for i in range(N):
    Ai = [int(i) for i in list(input())]
    A.append(Ai)
 
 
def lim_add(x, y, N):
    return (x + y) % N
 
 
def tate_a_next(i, j, N):
    i = lim_add(i, 1, N)
    return (i, j)
 
 
def tate_b_next(i, j, N):
    i = lim_add(i, -1, N)
    return (i, j)
 
 
def yoko_a_next(i, j, N):
    j = lim_add(j, 1, N)
    return (i, j)
 
 
def yoko_b_next(i, j, N):
    j = lim_add(j, -1, N)
    return (i, j)
 
 
def cross_a_next(i, j, N):
    i = lim_add(i, 1, N)
    j = lim_add(j, 1, N)
    return (i, j)
 
 
def cross_b_next(i, j, N):
    i = lim_add(i, 1, N)
    j = lim_add(j, -1, N)
    return (i, j)
 
 
def cross_c_next(i, j, N):
    i = lim_add(i, -1, N)
    j = lim_add(j, 1, N)
    return (i, j)
 
 
def cross_d_next(i, j, N):
    i = lim_add(i, -1, N)
    j = lim_add(j, -1, N)
    return (i, j)
 
 
anses = []
 
A_np = np.array(A)
 
 
def chk(f, i, j):
    anses.append(0)
    s = 0
    for _ in range(N):
        s = A[i][j] + s * 10
        i, j = f(i, j, N)
    anses[-1] = max(anses[-1], s)
 
 
for i in range(N):
    for j in range(N):
        chk(yoko_a_next, i, j)
        chk(yoko_b_next, i, j)
        chk(tate_a_next, i, j)
        chk(tate_b_next, i, j)
        chk(cross_a_next, i, j)
        chk(cross_b_next, i, j)
        chk(cross_c_next, i, j)
        chk(cross_d_next, i, j)
 
 
ans = max(anses)
print(ans)