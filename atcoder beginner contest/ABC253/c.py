from collections import deque

Q = int(input())
deque_ans = deque()
query = [list(map(int, input().split())) for _ in range(Q)]
for i in query:
    query_0 = i[0]
    
    if query_0 == 3:
        print(max(deque_ans) - min(deque_ans))
    elif query_0 == 1:
        deque_ans.appendleft(i[1])
    #2 x c : S から x を min(c, (S に含まれる x の個数 )) 個削除する。
    #2 2 3 : S から 2 を min(3, (S に含まれる 2 の個数 )) 個削除する。
    #2 2 3 : S から 2 を min(3, 2) 個削除する。
    elif query_0 == 2:
        for j in range(min(i[2],deque_ans.count(i[1]))):
            deque_ans.remove(i[1])