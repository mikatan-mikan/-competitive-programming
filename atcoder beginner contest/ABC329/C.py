n = int(input())

s = input()

cnt = 1

leng = [0 for _ in range(26)]#全てのアルファベットの最大長
bef_al = s[0]
leng[ord(bef_al) - 97] = 1
now_len = 1


for i in range(1,len(s)):
    if s[i] == bef_al:
        now_len += 1
    else:
        leng[ord(bef_al) - 97] = max(leng[ord(bef_al) - 97], now_len)
        bef_al = s[i]
        now_len = 1

leng[ord(bef_al) - 97] = max(leng[ord(bef_al) - 97], now_len)

ans = sum(leng)


print(ans)