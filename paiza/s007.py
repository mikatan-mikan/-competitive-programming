s = input()

num_check = set(["0","1","2","3","4","5","6","7","8","9"])

letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
sum_letter = {letters[i]:0 for i in range(len(letters))}


from collections import deque

now_magnification = 1#等倍
magnification = deque()#現在の文字列に対する倍率(数字が出てから"("が出るまでの数字を拾い上げる,)がでればpopする)
num_flg = False
num = deque()#拾い上げた数字を保管しておきn桁の数字を生成してからmagnificationに入れる

for i in range(len(s)):#前の文字から順に見る
    now = s[i]
    if s[i] in num_check:#数字なら
        num.append(int(s[i]))#数字を保管
        num_flg = True
    elif num_flg == True:#前回までが数字で今回がそうでなければ
        ml = 1
        n = 0
        while num:
            n += num.pop() * ml
            ml *= 10
        if s[i] == "(":
            now_magnification *= n
            magnification.append(n)
        else:#一文字だけに倍率の場合
            sum_letter[s[i]] += now_magnification * n
        num_flg = False
    elif s[i] == ")":
        #現在の倍率から前回の(時の倍率を無くし、現在の倍率を代入
        now_magnification //= magnification.pop()
    else:#普通の文字なら
        #現在の文字 倍率
        sum_letter[s[i]] += now_magnification
    


for i in letters:
    print(i,sum_letter[i])