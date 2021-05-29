# https://atcoder.jp/contests/jsc2021/tasks/jsc2021_b

n, m = map(int,input().split())
a = list(set(list(map(int,input().split()))))
b = list(set(list(map(int,input().split()))))

c = a + b
ans = []

for i in c:
  if c.count(i) == 1:
    ans.append(i)

ans.sort()
print(*ans)
