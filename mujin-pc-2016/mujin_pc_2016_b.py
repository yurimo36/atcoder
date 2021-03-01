# https://atcoder.jp/contests/mujin-pc-2016/tasks/mujin_pc_2016_b

import math

li = list(map(int,input().split()))
ans = (sum(li))**2 #最大の長さにした時の面積

a = sum(li) - max(li) #最大値以外の和
b = max(li) #最大値
if a < b:
    ans -= (b-a)**2

print(ans*math.pi)