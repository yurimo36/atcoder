# https://atcoder.jp/contests/abc093/tasks/arc094_a

li = list(map(int,input().split()))
x = max(li)

if (x*3-sum(li))%2 == 1: #目標までの差が奇数なら
    x += 1 #目標を1増やす

print((x*3-sum(li)+1)//2)