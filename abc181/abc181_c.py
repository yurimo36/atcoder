# https://atcoder.jp/contests/abc181/tasks/abc181_c

import itertools

n = int(input())
li = [list(map(int,input().split())) for i in range(n)]
c = itertools.combinations(li, 3)

for v in c:
    # (Ax*By+Bx*Cy+Cx*Ay)-(Ax*Cy+Bx*Ay+Cx*By)が三角形の面積 -> この値が0なら同一直線上
    if v[0][0]*v[1][1] + v[1][0]*v[2][1] + v[2][0]*v[0][1] == v[0][0]*v[2][1] + v[1][0]*v[0][1] + v[2][0]*v[1][1]:
        print("Yes")
        exit()

print("No")
