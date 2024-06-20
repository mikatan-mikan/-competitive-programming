n = int(input())
a = list(map(int,input().split()))

from sortedcontainers import SortedList
exist_l = SortedList([[i,a[i]] for i in range(n)])
exist = {a[i]:i for i in range(n)}

q = int(input())

for i in range(q):
    query = list(map(int,input().split()))
    if query[0] == 1:
        exist_l.add([query[1],query[2]])
        exist[query[2]] = query[1]
    elif query[0] == 2:
        if query[1] in exist_l:
            print("Yes")
        else:
            print("No")