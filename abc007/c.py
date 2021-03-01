# https://atcoder.jp/contests/abc007/tasks/abc007_3

h, w = map(int,input().split())
a, b = map(int,input().split())
c, d = map(int,input().split())
li = [list(input()) for i in range(h)]
houmon = [[-1 for i in range(w)] for j in range(h)]
houmon[a-1][b-1] = 0
que = [[a-1, b-1]]

while True:
    now = que.pop(0)
    y = now[0]
    x = now[1]
    z = houmon[y][x]

    for i in range(y-1, y+2):
        for j in range(x-1, x+2):
            if (i != y and j != x) or (i == y and j == x):
                continue #5/9を排除
            if i == c-1 and j == d-1: #ゴール地点なら
                print(z+1)
                exit()
            if li[i][j] == "." and houmon[i][j] == -1: #到達可能で未踏なら
                que.append([i,j])
                houmon[i][j] = z+1
