# https://atcoder.jp/contests/abc010/tasks/abc010_2

n = int(input())
a = list(map(int,input().split()))
l = [0, 1, 0, 1, 2, 3, 0, 1, 0]
ans = 0

for i in a:
    ans = ans + l[i-1]

print(ans)