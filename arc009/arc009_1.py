# https://atcoder.jp/contests/arc009/tasks/arc009_1

n = int(input())
li = [list(map(int,input().split())) for i in range(n)]
ans = 0

for l in li:
    ans += l[0]*l[1]

ans *= 1.05
print(int(ans))