# https://atcoder.jp/contests/abc047/tasks/abc047_b

import itertools

w, h, n = map(int,input().split())
now = [[1]*w]*h
li = [list(map(int,input().split())) for i in range(n)]

for x in li:
    if x[2]==1: #x以下を塗りつぶす
        for i in range(h):
            for j in range(x[0]):
                now[i][j] = 0
    if x[2]==2: #x以上を塗りつぶす
        for i in range(h):
            for j in range(w-x[0]):
                now[i][x[0]+j] = 0
    if x[2]==3: #y以下を塗りつぶす
        for i in range(x[1]):
            now[i] = [0]*w
    if x[2]==4: #y以上を塗りつぶす
        for i in range(x[1],h):
            now[i] = [0]*w

print(sum(list(itertools.chain.from_iterable(now))))
