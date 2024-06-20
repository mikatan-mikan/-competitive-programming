n = int(input())

a = list(map(int,input().split()))

# ソート前の位置と要素の対応を保存する辞書
original_positions = {value: index for index, value in enumerate(a)}

# ソート後のリスト
b = sorted(a)

# ソート後の位置と要素の対応を保存する辞書
sorted_positions = {value: index for index, value in enumerate(b)}

sum_ = sum(a)
ptr = 1
minus = 0
sum__ = 0

# 今回のものをsum_から減算した後に、bのうち前からどこまでがa[i]を引いても0以上なのかを見て
# 0未満なら下回った分だけminusを加算しておく
for i in range(n - 1):
    sum_ -= a[i]

    while True:
        if b[ptr] - a[i] < 0:
            minus += b[ptr] - a[i]
            ptr += 1
        else:
            break
    sum__ += (sum_ - (len(a) - (i + 1)) * a[i]) - minus

print(sum__)