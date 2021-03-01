# https://atcoder.jp/contests/arc004/tasks/arc004_1

n = int(input())
li =[list(map(int,input().split())) for i in range(n)]
ans = 0.0

for i in range(n):
	for j in range(n):
		x = ((li[i][0]-li[j][0])**2 + (li[i][1]-li[j][1])**2)**0.5
		if x > ans:
			ans = x

print(ans)