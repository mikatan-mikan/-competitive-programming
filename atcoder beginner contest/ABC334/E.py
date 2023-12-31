def binary_search_for_max_value(arr, target):
    left, right = 0, len(arr) - 1
    result = -1  # 初期値は条件を満たさない値

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] < target:
            # 中央の値が目標より小さい場合、結果を更新して右半分を探索
            result = arr[mid]
            left = mid + 1
        else:
            # 中央の値が目標以上の場合、左半分を探索
            right = mid - 1

    return result

# 例
arr = [1, 3, 5, 7, 8, 9, 11, 13, 15]
current_value = 8
result = binary_search_for_max_value(arr, current_value)

print("最大の値:", result)