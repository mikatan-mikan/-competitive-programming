n,t_d = map(str,input().split())

n = int(n)

s = [input() for _ in range(n)]

from collections import deque

t_len = len(t_d)

ans = deque()
cnt = 0

for i in range(n):
    s_len = len(s[i])
    if s_len == t_len:
        dcnt = 0
        for j in range(s_len):
            if s[i][j] == t_d[j]:#文字一致
                continue
            else:#一文字置き換え
                dcnt += 1
                if dcnt >= 2:
                    break
        if dcnt < 2:
            ans.append(i + 1)
            cnt += 1
    elif s_len == t_len - 1:
        offset = 0
        for j in range(s_len):
            if s[i][j] == t_d[j + offset]:#文字一致
                continue
            else:#一文字挿入する
                offset += 1
                if offset >= 2:
                    break
                if s[i][j] == t_d[j + offset]:#文字一致
                    continue
                else:
                    offset = 2
                    break
        if offset <= 1:
            ans.append(i + 1)
            cnt += 1
    elif s_len == t_len + 1:
        offset = 0
        for j in range(t_len):
            if s[i][j + offset] == t_d[j]:#文字一致
                continue
            else:#一文字挿入する
                offset += 1
                if offset >= 2:
                    break
                if s[i][j + offset] == t_d[j]:#文字一致
                    continue
                else:
                    offset = 2
                    break
        if offset <= 1:
            ans.append(i + 1)
            cnt += 1

print(cnt)
print(*ans)