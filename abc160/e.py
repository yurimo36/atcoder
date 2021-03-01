# https://atcoder.jp/contests/abc160/tasks/abc160_e

x, y, a, b, c = map(int,input().split())
p = list(map(int,input().split()))
q = list(map(int,input().split()))
r = list(map(int,input().split()))

p.sort(reverse=True)
q.sort(reverse=True)

r = p[:x] + q[:y] + r
r.sort(reverse=True)
r = r[:x+y]

print(sum(r))