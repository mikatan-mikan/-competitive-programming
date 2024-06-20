n,x = map(int,input().split())

t = list(map(int,input().split()))


time_que = [0 for _ in range(x + 2)]#現在の時間にどれだけのqueが存在するのか
time_que[0] = 1#0秒目には曲を流し始めるため、queを追加する

music_1 = 0
music_other = 0

for now in range(x + 2):#i秒目(x + 0.5秒を見る必要があるため0...x + 1まで)
    if time_que[now] >= 1:#1回以上のqueが予約されているなら
        for j in range(len(t)):
            if now + t[j] < x + 2:
                #time_queのnow+t[i]番目を+=1し、後に処理する
                time_que[now + t[j]] += (1 * time_que[now])
            else:#オーバーするならそれが最後の曲なので
                if j == 0:
                    music_1 += time_que[now]
                else:
                    music_other += time_que[now]

print((music_1,music_other))
