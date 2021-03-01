# https://atcoder.jp/contests/abc009/tasks/abc009_2

n = int(input())
a = [int(input()) for i in range(n)]
a = list(set(a))
a.sort(reverse=True)
print(a[1])