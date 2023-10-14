N = int(input())

ans = [3.5]
dice = [6,5,4,3,2,1]

for i in range(N - 1):#初期のはやってるので
    next_up = 6 - int(ans[i])#次に数字が前回の期待値より上がる出目の数
    next_num = sum(dice[:next_up]) / next_up#次回数値が上がるときの平均値
    probability = next_up / 6 # 次回数字が上がる確率
    ans.append(ans[i] + (next_num - ans[i]) * probability)

print(max(ans))