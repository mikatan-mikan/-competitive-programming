from collections import deque

N = int(input())

S = deque()


for i in range(N):
    S.append(input())

save_in = dict()
#何が何個あったかのデータを作る
for i in range(N):
    out = S.count(S[i])#中に何個あるかを探索
    try:
        save_in[S[i]]
        save_in.update({f"{S[i]}" : save_in[S[i]]})
    except:
        save_in.update({f"{S[i]}" : 0}) #S[i]はout個存在し、現在count回表示している
    if save_in[S[i]] == 0:
        print(S[i])
    else:
        print(S[i] + "(" + str(save_in[S[i]]) + ")")
    save_in[S[i]] += 1