# https://atcoder.jp/contests/abc088/tasks/abc088_b

n = int(input())
li = list(map(int,input().split()))
li.sort(reverse=True)
a = []
b = []

for i in range(n):
  if i%2 == 0:
    a.append(li[i])
  else:
    b.append(li[i])

print(sum(a)-sum(b))