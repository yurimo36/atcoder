# https://atcoder.jp/contests/abc066/tasks/abc066_a

li = list(map(int,input().split()))
li.sort()
print(sum(li[:2]))