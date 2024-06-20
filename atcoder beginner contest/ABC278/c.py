N,Q = map(int,input().split())

follow_set = set()#フォロデータをした方,された方のタプルで
for i in range(Q):
    T,A,B = map(int,input().split())#入ってくる操作
    if T == 1:
        follow_set.add((A,B))
    if T == 2:
        if (A,B) in follow_set:
            follow_set.remove((A,B))
    if T == 3:
        if (A,B) in follow_set and (B,A) in follow_set:
            print("Yes")
        else:
            print("No")