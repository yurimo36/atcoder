# https://atcoder.jp/contests/abc185/tasks/abc185_b

n, m, t = map(int,input().split())
ima = n
li = [list(map(int,input().split())) for i in range(m)] + [[t, 0]]
x = 0

for l in li:
    ima -= l[0]-x
    if ima <= 0:
        print("No")
        exit()
    ima = min(ima+l[1]-l[0], n)
    x = l[1]

print("Yes")
