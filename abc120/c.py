# https://atcoder.jp/contests/abc120/tasks/abc120_c

s = input()
n = len(s)

x = s.count("0")
y = s.count("1")

print(min(x,y)*2)