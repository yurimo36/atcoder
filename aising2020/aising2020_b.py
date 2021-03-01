# https://atcoder.jp/contests/aising2020/tasks/aising2020_b

n = int(input())
li = list(map(int,input().split()))
ans = 0

for i in range(n):
    if i%2 == 0:
        if li[i]%2 == 1:
            ans += 1

print(ans)