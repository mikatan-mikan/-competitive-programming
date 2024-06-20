N = int(input())

p_list = list(map(int,input().split()))

cnt = 0
now_p = N - 2#現在親を探している人(2から始まるので1引く + 1から考える)
while True:#一世代にたどり着くまで
    now_p = p_list[now_p] - 2
    cnt += 1
    if now_p == -1:
        break

print(cnt)