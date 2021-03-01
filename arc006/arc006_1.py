# https://atcoder.jp/contests/arc006/tasks/arc006_1

e = list(map(int,input().split()))
b = int(input())
l = list(map(int,input().split()))
ans = 0

for i in range(10):
	if i in e and i in l:
		ans += 1

if ans == 6:
	print(1)

elif ans == 5:
	if b in l:
		print(2)
	else:
		print(3)

elif ans == 4:
	print(4)

elif ans == 3:
	print(5)

else:
	print(0)