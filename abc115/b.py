# https://atcoder.jp/contests/abc115/tasks/abc115_b

n = int(input())
p = [int(input()) for i in range(n)]

print(sum(p) - max(p)//2)