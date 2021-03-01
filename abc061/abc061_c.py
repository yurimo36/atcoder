# https://atcoder.jp/contests/abc061/tasks/abc061_c

n, k = map(int,input().split())
ans  = []
x = 0

for i in range(n):
    ans.append(list(map(int,input().split())))

ans.sort()

for l in ans:
    x += l[1]
    if x < k:
        continue
    else:
        print(l[0])
        exit()