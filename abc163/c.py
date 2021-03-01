# https://atcoder.jp/contests/abc163/tasks/abc163_c

n = int(input())
a = list(map(int,input().split()))
ans = [0]*n

for i in a:
    ans[i-1] = ans[i-1] + 1

for i in ans:
    print(i)