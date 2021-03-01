# https://atcoder.jp/contests/code-festival-2017-qualc/tasks/code_festival_2017_qualc_b

n = int(input())
li = list(map(int,input().split()))
ans = 3**n
x = 1

for i in li:
    if i%2 == 0:
        x *= 2

print(ans-x)