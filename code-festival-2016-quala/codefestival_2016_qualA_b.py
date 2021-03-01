# https://atcoder.jp/contests/code-festival-2016-quala/tasks/codefestival_2016_qualA_b

n = int(input())
li = list(map(int,input().split()))
ans = 0

for i in range(n):
    x = li[i]
    if li[x-1] == i+1:
        ans += 1

print(ans//2)