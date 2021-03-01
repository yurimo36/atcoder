# https://atcoder.jp/contests/abc171/tasks/abc171_e

n = int(input())
li = list(map(int,input().split()))
s = li[0]
ans = []

for i in range(n-1):
    s = s ^ li[i+1]

for i in li:
    ans.append(s ^ i)

print(*ans)