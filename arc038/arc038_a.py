# https://atcoder.jp/contests/arc038/tasks/arc038_a

n = int(input())
li = list(map(int,input().split()))

li.sort(reverse=True)
print(sum(li[::2]))