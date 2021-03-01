# https://atcoder.jp/contests/arc004/tasks/arc004_2

n = int(input())
li =[int(input()) for i in range(n)]
x = sum(li)
y = max(li)
z = x-y

if z >= y:
	y = 0
else:
	y -= z

print(x)
print(y)