s, t = input().split()

# 文字列Sの長さを取得
len_s = len(s)

for w in range(1, len_s):
    s_s = [s[i:i+w] for i in range(0, len_s, w)]
    
    for c in range(1, w + 1):
        t_s = []
        for se in s_s:
            if len(se) >= c:
                t_s.append(se[c-1])
        if "".join(t_s) == t:
            print("Yes")
            exit()

print("No")