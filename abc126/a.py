# https://atcoder.jp/contests/abc126/tasks/abc126_a

n, k = map(int,input().split())
s = input()
print(s[:k-1] + s.lower()[k-1] + s[k:n])
