# https://atcoder.jp/contests/abc105/tasks/abc105_b

n = int(input())

for i in range(0, n//4+1):
  if (n - i*4) % 7 == 0:
    print("Yes")
    exit()
print("No")