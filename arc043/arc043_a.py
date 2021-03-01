# https://atcoder.jp/contests/arc043/tasks/arc043_a

n, a, b = map(int,input().split())
li = [int(input()) for i in range(n)]
x = max(li) - min(li) #最大値と最小値の差
y = sum(li)/n #平均値

if x == 0:
    print(-1)
    exit()

b /= x
a -= b*y

print(b, a)