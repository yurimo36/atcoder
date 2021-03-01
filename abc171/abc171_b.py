# https://atcoder.jp/contests/abc171/tasks/abc171_b

x, y = map(int,input().split())
li = list(map(int,input().split()))
li.sort()
print(sum(li[:y]))