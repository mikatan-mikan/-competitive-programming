from collections import deque

N = int(input())

S = deque()

save_in = dict()
for i in range(N):
    S.append(input())
    try:
        save_in[S[i]]
    except:
        save_in.update({f"{S[i]}" : 0})
    if save_in[S[i]] == 0:
        print(S[i])
    else:
        print(S[i] + "(" + str(save_in[S[i]]) + ")")
    save_in[S[i]] += 1