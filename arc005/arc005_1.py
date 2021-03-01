# https://atcoder.jp/contests/arc005/tasks/arc005_1

n = int(input())
li = input().split()
ans = 0

for i in range(n):
	if li[i] == "TAKAHASHIKUN" or li[i] == "Takahashikun" or li[i] == "takahashikun":
		ans += 1
	if i == n-1 and (li[i] == "TAKAHASHIKUN." or li[i] == "Takahashikun." or li[i] == "takahashikun."):
		ans += 1

print(ans)