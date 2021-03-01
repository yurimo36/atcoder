# https://atcoder.jp/contests/abc128/tasks/abc128_c

n, m = map(int,input().split())
li = [list(map(int,input().split()))[1:] for i in range(m)]
p = list(map(int,input().split()))
ans = 0

for i in range(2 ** n):
    x = 0 #点灯してるかしてないか
    y = [[] for j in range(m)]
    for j in range(n):
        if ((i >> j) & 1): #フラグが立っていたら=スイッチon 
            for k in range(m):
                if j+1 in li[k]:
                    y[k].append(j+1)
    for j in range(m):
        if len(y[j]) %2 == p[j]:
            x += 1                   
    if x == m:
        ans += 1

print(ans)