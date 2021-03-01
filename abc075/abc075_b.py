# https://atcoder.jp/contests/abc075/tasks/abc075_b

h, w = map(int,input().split())
ans= [list(input()) for i in range(h)]

for i in range(h):
    for j in range(w):
        if ans[i][j] !="#": #その升が爆弾じゃなかったら
            count = 0
            for p in range(max(0,i-1), min(i+2, h)):
                for q in range(max(0,j-1), min(j+2, w)):
                    if ans[p][q] == "#":
                        count += 1
            ans[i][j] = str(count)

for l in ans:
    for c in l:
        print(c, end="")
    print()