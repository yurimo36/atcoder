# https://atcoder.jp/contests/abc179/tasks/abc179_b

n = int(input())
count = 0
ans = "No"

for i in range(n):
    x, y = map(int,input().split())
    if x == y:
        count += 1
    else:
        count = 0
    if count == 3:
        ans = "Yes"

print(ans)
