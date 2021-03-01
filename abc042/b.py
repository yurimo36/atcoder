# https://atcoder.jp/contests/abc042/tasks/abc042_b

n, l = map(int,input().split())
li = [input() for i in range(n)]
ans = ""
li.sort()

for s in li:
  ans += s
  
print(ans)