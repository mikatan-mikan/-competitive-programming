N,M = map(int,input().split())

S = list()
T = set()
Ans_set = list()

loop_range = list(range(N))

for i in loop_range:
    S.append(input())

for i in range(M):
    T.add(input())

if N==1:
    for i in loop_range:#全部の文字列が最初であるとして
        Ans_set.append(S[i])
    for i in range(len(Ans_set)):
        if Ans_set[i] not in T:
            print(Ans_set[i])
            exit()

if N==2:
    for i in loop_range:#全部の文字列が最初であるとして
        for j in loop_range:#二つ目の文字列
            if i == j:
                continue
            Ans_set.append(S[i] + "_" + S[j])
    for i in range(len(Ans_set)):
        if Ans_set[i] not in T:
            print(Ans_set[i])
            exit()

if N==3:
    for i in loop_range:#全部の文字列が最初であるとして
        for j in loop_range:#二つ目の文字列
            if i == j:
                continue
            for k in loop_range:#3つ目の文字列
                if j == k:
                    continue
                Ans_set.append(S[i] + "_" + S[j] + "_" + S[k])
    for i in range(len(Ans_set)):
        if Ans_set[i] not in T:
            print(Ans_set[i])
            exit()

if N==4:
    for i in loop_range:#全部の文字列が最初であるとして
        for j in loop_range:#二つ目の文字列
            if i == j:
                continue
            for k in loop_range:#3つ目の文字列
                if j == k:
                    continue
                for l in loop_range:
                    if k == l:
                        continue
                    Ans_set.append(S[i] + "_" + S[j] + "_" + S[k] + "_" + S[l])
    for i in range(len(Ans_set)):
        if Ans_set[i] not in T:
            print(Ans_set)
            exit()

if N==5:
    for i in loop_range:#全部の文字列が最初であるとして
        for j in loop_range:#二つ目の文字列
            if i == j:
                continue
            for k in loop_range:#3つ目の文字列
                if j == k:
                    continue
                for l in loop_range:
                    if k == l:
                        continue
                    for m in loop_range:
                        if l == m:
                            continue
                        Ans_set.append(S[i] + "_" + S[j] + "_" + S[k] + "_" + S[l] + "_" + S[m])
    for i in range(len(Ans_set)):
        if Ans_set[i] not in T:
            print(Ans_set)
            exit()

if N==6:
    for i in loop_range:#全部の文字列が最初であるとして
        for j in loop_range:#二つ目の文字列
            if i == j:
                continue
            for k in loop_range:#3つ目の文字列
                if j == k:
                    continue
                for l in loop_range:
                    if k == l:
                        continue
                    for m in loop_range:
                        if l == m:
                            continue
                        for n in loop_range:
                            if m == n:
                                continue
                            Ans_set.append(S[i] + "_" + S[j] + "_" + S[k] + "_" + S[l] + "_" + S[m] + "_" + S[n])
    for i in range(len(Ans_set)):
        if Ans_set[i] not in T:
            print(Ans_set)
            exit()



if N==7:
    for i in loop_range:#全部の文字列が最初であるとして
        for j in loop_range:#二つ目の文字列
            if i == j:
                continue
            for k in loop_range:#3つ目の文字列
                if j == k:
                    continue
                for l in loop_range:
                    if k == l:
                        continue
                    for m in loop_range:
                        if l == m:
                            continue
                        for n in loop_range:
                            if m == n:
                                continue
                            for z in loop_range:
                                if n == z:
                                    continue
                            Ans_set.append(S[i] + "_" + S[j] + "_" + S[k] + "_" + S[l] + "_" + S[m] + "_" + S[n] + "_" + S[z])
    for i in range(len(Ans_set)):
        if Ans_set[i] not in T:
            print(Ans_set)
            exit()

if N==8:
    for i in loop_range:#全部の文字列が最初であるとして
        for j in loop_range:#二つ目の文字列
            if i == j:
                continue
            for k in loop_range:#3つ目の文字列
                if j == k:
                    continue
                for l in loop_range:
                    if k == l:
                        continue
                    for m in loop_range:
                        if l == m:
                            continue
                        for n in loop_range:
                            if m == n:
                                continue
                            for z in loop_range:
                                if n == z:
                                    continue
                                for p in loop_range:
                                    if z == p:
                                        continue
                            Ans_set.append(S[i] + "_" + S[j] + "_" + S[k] + "_" + S[l] + "_" + S[m] + "_" + S[n] + "_" + S[z] + "_" + S[p])
    for i in range(len(Ans_set)):
        if Ans_set[i] not in T:
            print(Ans_set)
            exit()

print(-1)