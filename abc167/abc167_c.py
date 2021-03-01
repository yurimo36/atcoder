# https://atcoder.jp/contests/abc167/tasks/abc167_c

import numpy as np

def python_list_add(in1, in2):
    wrk = np.array(in1) + np.array(in2)
    return wrk.tolist()

n, m, x = map(int,input().split())
li = [list(map(int,input().split())) for i in range(n)]
 #価格の合計
ans = []

for i in range(2 ** n):
    bag = []
    for j in range(n):  # このループが一番のポイント
        if ((i >> j) & 1):  # 順に右にシフトさせ最下位bitのチェックを行う
            bag.append(j)  # フラグが立っていたら bag に果物を詰める
    
    p = 0
    org = [0]*m
    for k in bag:
        p += li[k][0]
        pos = li[k][1:]
        org = python_list_add(org, pos)
    if all(l >= x for l in org): #条件を満たしていたら
        ans.append(p)


if len(ans) == 0:
    print(-1)
else:
    print(min(ans))