N = int(input())
A = list(map(int,input().split()))
change_flag = set()#ここに入ってるのは既に前回の1クエリ以降に書き換えられてる
next_num = 0

Q = int(input())

for i in range(Q):
    Query = list(map(int,input().split()))
    if Query[0] == 1:
        change_flag.clear()
        next_num = Query[1]
    elif Query[0] == 2:
        if Query[1] not in change_flag and next_num != 0:
            A[Query[1] - 1] = (Query[2] + next_num)
            change_flag.add(Query[1])
        else:
            A[Query[1] - 1] += Query[2]
    else:
        if Query[1] not in change_flag and next_num != 0:
            print(next_num)
        else:
            print(A[Query[1] - 1])