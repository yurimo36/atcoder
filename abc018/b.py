# https://atcoder.jp/contests/abc018/tasks/abc018_2

s = input()
n = int(input())

for i in range(n):
  x, y = map(int,input().split())
  s = s[:x-1] + s[x-1:y][::-1] + s[y:]

print(s)