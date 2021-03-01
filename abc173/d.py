# https://atcoder.jp/contests/abc173/tasks/abc173_d

n = int(input())
li = list(map(int,input().split()))
li.sort(reverse=True)
ans = 0

for i in range(n//2):
    if i == 0:
        ans += li[i]
    else:
        ans += li[i]*2

if n%2 == 1:
    ans += li[i+1]

print(ans)
