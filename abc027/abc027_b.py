# https://atcoder.jp/contests/abc027/tasks/abc027_b

n = int(input())
li = list(map(int,input().split()))
x = sum(li)
ans = 0

if x%n != 0:
    print(-1)
    exit()

y = x//n

for i in range(1,n):
    a = li[:i]
    if sum(a) != y*len(a):
        ans += 1

print(ans)
