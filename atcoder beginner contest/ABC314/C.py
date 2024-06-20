n,m = map(int,input().split())

s = input()

c = list(map(int,input().split()))

color_letters = [[] for _ in range(m + 1)]#i番目のlistにはi色の文字を順に並べたものが入る
color_letters_buffer = [-1 for _ in range(n + 1)]#次に出力する場所

for i in range(len(c)):
    color_letters[c[i]].append(s[i])#色の番号番目にその文字を追加


for i in range(len(c)):
    print(color_letters[c[i]][color_letters_buffer[c[i]]],end="")
    color_letters_buffer[c[i]] += 1