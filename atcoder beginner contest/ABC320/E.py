N,M = map(int,input().split())


from collections import deque

# N 人の初期位置を設定
positions = deque(range(1, N+1))

cooltime = {}

# 人々のそうめんの獲得量を記録するリストを作成
soymen_gained = [0] * N

# M 回の出来事を処理
for i in range(M):
    # 時刻 Ti と量 Wi を取得
    Ti, Wi, Si = map(int, input().split())
    
    # 列の先頭の人がそうめんを得る
    soymen_gained[positions[0] - 1] += Wi
    
    # 列から先頭の人を削除
    cooltime[str(Ti + Si)] = positions.popleft()
    
    # 次の出来事まで待つ
    wait_time = Ti + Si
    while positions and positions[0] <= wait_time:
        positions.pop()
    
    # 待ち時間後に列の元の位置に戻す
    positions.appendleft(i + 1)

# 各人のそうめんの獲得量を出力
for amount in soymen_gained:
    print(amount)