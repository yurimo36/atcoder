# https://atcoder.jp/contests/abc133/tasks/abc133_c

i, j = map(int,input().split())
ans = 100000000

for m in range(i, min(j, i+2019)): #高々O(2019**2)
  for n in range(m+1, min(j+1, i+2020)):
    x = m * n % 2019
    if x < ans:
      ans = x

print(ans)