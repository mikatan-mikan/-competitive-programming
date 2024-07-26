n,k = map(int,input().split())
s = input()

ans = 1

#ごりごりみてよさそう
for i in range(k,n):#文字長
    #?でない場合そこから5文字が回文でないかを判定する
    if "?" in s[i - (k):i] or s[i - (k):i] != s[i - (k):i][::-1]:
        continue
    else:
        #回文が存在してしまっている
        print(0)
        exit()

for i in range(n):
    if s[i] != "?":
        continue
    #?であればそこをAとBどちらに変えても大丈夫かを判定する
    safety = [0,0]
    for j in range(k):#全通りの開始地点から探索
        if i - j + k > n or i - j < 0:
            safety[0] += 1
            safety[1] += 1
            continue
        now_a = list(s[i - j:i - j + k])
        now_b = list(s[i - j:i - j + k])
        now_a[j] = "A"
        now_b[j] = "B"
        sp = 0
        for l in range(k):
            if now_a[l] == "?":
                now_a[l] = str(sp)
                sp += 1
            if now_b[l] == "?":
                now_b[l] = str(sp)
                sp += 1
        bef_ans = safety.copy()
        if now_a != now_a[::-1]:
            safety[0] += 1
        if now_b != now_b[::-1]:
            safety[1] += 1
        if safety == bef_ans:
            #同じ結果が出てきていれば = a,bどちらにしても回文であれば
            print(0)
            exit()
    if safety == [k,k]:#2通り両方いける場合通り数が増える
        ans *= 2
    elif k not in safety:#両方使えない場合 = どちらにしても回文
        print(0)
        exit()
    else:#そうでなくてexitしていない = a,bどちらかは回文ではないなら
        if safety[0] == k:
            s = s[:i] + "A" + s[i + 1:]
        else:
            s = s[:i] + "B" + s[i + 1:]

print(ans % 998244353)