n,t = map(int,input().split())

players_score = [0 for _ in range(n + 1)]#それぞれの人のスコア
score = {0:n}#それぞれのスコアが何人いるか
score_ = set([0])#種類

for i in range(t):
    a,b = map(int,input().split())

    if b + players_score[a] in score_:#既にスコアに含まれている場合
        #そのスコアの数を増やす
        score[b + players_score[a]] += 1
        
    else:
        score[b + players_score[a]] = 1
        score_.add(b + players_score[a])

    #前のスコアの数を減らす
    score[players_score[a]] -= 1
    #もし前のスコアがゼロ人なら
    if score[players_score[a]] == 0:
        #score_とscoreの要素を削除
        score_.remove(players_score[a])
        score.pop(players_score[a])

    players_score[a] += b

    print(len(score_))