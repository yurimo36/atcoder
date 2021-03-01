# https://atcoder.jp/contests/code-festival-2015-quala/tasks/codefestival_2015_qualA_b

n = int(input())
li = list(map(int,input().split()))
ans = 0

for i in range(n):
    ans = ans*2 + li[i]

print(ans)