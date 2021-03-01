# https://atcoder.jp/contests/m-solutions2019/tasks/m_solutions2019_b

s = input()
n = len(s)

if s.count("o") >= 8-(15-n):
  print("YES")
else:
  print("NO")