# https://atcoder.jp/contests/nomura2020/tasks/nomura2020_a

h1, m1, h2, m2, k = map(int,input().split())

if m1 > m2:
    x = (h2 - h1 - 1)*60 + m2 - m1 + 60 - k

else:
    x = (h2 - h1)*60 + m2 - m1- k

print(x)