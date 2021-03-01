# https://atcoder.jp/contests/abc152/tasks/abc152_c

n = int(input())
p = list(map(int,input().split()))
mini = p[0]
ans = 1

for i in p:
    if i < mini:
        ans += 1
        mini = i

print(ans)