# https://atcoder.jp/contests/abc200/tasks/abc200_c

n = int(input())
a = list(map(int,input().split()))
li = [0 for i in range(200)]
ans = 0

for i in a:
  li[i%200] += 1

for i in li:
  if i > 1:
    ans += i*(i-1)//2

print(ans)
