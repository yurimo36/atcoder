# https://atcoder.jp/contests/code-festival-2014-qualb/tasks/code_festival_qualB_b

n, k = map(int,input().split())
li = [int(input()) for i in range(n)]
x = 0

for i in range(n):
    x += li[i]
    if x >= k:
        print(i+1)
        break