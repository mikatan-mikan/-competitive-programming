from collections import deque
from sys import stdin

A = deque()
note = dict()
Ans = deque()

Q = int(input())

for i in range(Q):
    query = stdin.readline()[:-1]
    if query[0:3] == "ADD":
        A.append(int(query[4:]))
    if query == "DELETE":
        if len(A) > 0:
            A.pop()
    if query[0:4] == "SAVE":
        note[query[5:]] = A.copy()
    if query[0:4] == "LOAD":
        try:
            A = note[query[5:]]
        except: A = deque()
    try:
        Ans.append(A[-1])
    except: Ans.append(-1)


print(* Ans)