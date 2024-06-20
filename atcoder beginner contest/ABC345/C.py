s = input()

#全てのアルファベットの数をカウント
alpha = {"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0,"h":0,"i":0,"j":0,"k":0,"l":0,"m":0,"n":0,"o":0,"p":0,"q":0,"r":0,"s":0,"t":0,"u":0,"v":0,"w":0,"x":0,"y":0,"z":0}
for i in range(len(s)):
    alpha[s[i]] += 1

ans = 0

#いずれかのアルファベットの数が2個なら同じ文字列を生成できるので確認する
for i in range(97,123):
    if alpha[chr(i)] >= 2:
        ans += 1
        break

for i in range(len(s)):
    ans += (len(s) - (i)) - alpha[s[i]]
    alpha[s[i]] -= 1

print(ans)