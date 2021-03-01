# https://atcoder.jp/contests/abc151/tasks/abc151_c

n, m = map(int,input().split())
li = [0] * n
wa = 0
ac = 0

for i in range(m):
    p, s = map(str, input().split())
    p = int(p)

    if s == "WA" and li[p-1] >= 0: #WAかつ正解前
        li[p-1] += 1 #その問題をWAした数+1
    
    elif s == "AC" and li[p-1] >= 0: #ACかつ正解前
        wa += li[p-1] #それまでにWAした数をカウントに追加
        li[p-1] = -1 #ステータスを正解済に変更
        ac += 1 #AC+1

print(ac, wa)
