# https://atcoder.jp/contests/abc116/tasks/abc116_a

l = list(map(int,input().split()))
l.remove(max(l))

print(int(l[0]*l[1]/2))