# https://atcoder.jp/contests/m-solutions2020/tasks/m_solutions2020_c

n, k = map(int,input().split())
li = list(map(int,input().split()))

for i in range(n-k):
  if li[i] < li[i+k]:
    print("Yes")
  else:
    print("No")
