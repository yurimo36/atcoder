# https://atcoder.jp/contests/abc130/tasks/abc130_d

n, k = map(int,input().split())
li = list(map(int,input().split()))
ans = 0

x = 0
y = 0
s = li[0]

#しゃくとり法
while True:
    #print(x,y,s)
    if s < k: #もし合計がk未満だったら
        y += 1
        if y == n:
            break
        else:
            s += li[y]
    else: #k以上だったら
        ans += n-y
        s -= li[x]
        x += 1

print(ans)