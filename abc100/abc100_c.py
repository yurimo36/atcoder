# https://atcoder.jp/contests/abc100/tasks/abc100_c

n = int(input())
li = list(map(int,input().split()))
ans = 0

for i in li:
  while i%2 == 0:
    i = i//2
    ans += 1

print(ans)