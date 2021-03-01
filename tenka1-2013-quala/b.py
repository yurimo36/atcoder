# https://atcoder.jp/contests/tenka1-2013-quala/tasks/tenka1_2013_qualA_b

n = int(input())
li = [list(map(int,input().split())) for i in range(n)]
ans = 0

for l in li:
    if sum(l) < 20:
        ans += 1

print(ans)