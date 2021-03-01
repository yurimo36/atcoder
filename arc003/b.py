# https://atcoder.jp/contests/arc003/tasks/arc003_2

n = int(input())
li =[input()[::-1] for i in range(n)]
li.sort()

for w in li:
	print(w[::-1])