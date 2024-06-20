# ソート前のリスト
a = [3, 1, 4, 1, 5, 9, 2, 6]

# ソート前の位置と要素の対応を保存する辞書
original_positions = {value: index for index, value in enumerate(a)}

# ソート後のリスト
b = sorted(a)

# ソート後の位置と要素の対応を保存する辞書
sorted_positions = {value: index for index, value in enumerate(b)}

# ソート前の位置とソート後の位置の対応を表示
for value in original_positions:
    print(f"要素 {value}: ソート前の位置 {original_positions[value]} -> ソート後の位置 {sorted_positions[value]}")

print(b)