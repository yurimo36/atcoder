# https://atcoder.jp/contests/abc133/tasks/abc133_b

import math

n, d = map(int,input().split())
x=[]
ans = 0
y = 0.0

for i in range(n):
    x.append(list(map(int,input().split()))) #リストに加える
    
for i in range(n):
    for j in range(i+1,n): #それより前にリストに入っていたものについて
        y = 0.0
        for k in range(d): #次元数だけループ
            y = y + (x[i][k] - x[j][k])**2 #距離を計算
        if math.sqrt(y).is_integer() == True: #距離が整数なら
            ans = ans + 1 #答えに1を加える

print(ans)