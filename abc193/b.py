# https://atcoder.jp/contests/abc193/tasks/abc193_b

n = int(input())
li = [list(map(int,input().split())) for i in range(n)]
sort = sorted(li, key=lambda x: x[1])

for l in sort:
    if l[2]-l[0] > 0:
        print(l[1])
        exit()

print(-1)
