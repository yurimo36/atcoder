# https://atcoder.jp/contests/agc001/tasks/agc001_a

n = int(input())
li = list(map(int,input().split()))

li.sort()

print(sum(li[::2]))