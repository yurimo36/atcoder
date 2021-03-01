# https://atcoder.jp/contests/abc173/tasks/abc173_c

import copy
import itertools

h, w, k = map(int,input().split())
li = [list(input()) for i in range(h)]
ans = 0


#ビット全探索
for i in range(2**h):
    for j in range(2**w):
        x = copy.deepcopy(li)
        count = 0

        for b in range(h):
            if ((i >> b) & 1): #フラグが立っていたら
                x[b] = ["-"] * w
        for b in range(w):
            if ((j >> b) & 1): #フラグが立っていたら
                for a in range(h):
                    x[a][b] = "-"
        
        x = list(itertools.chain.from_iterable(x))
        if x.count("#") == k:
            ans += 1


print(ans)