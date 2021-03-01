# https://atcoder.jp/contests/abc163/tasks/abc163_b

n, m = map(int,input().split())
li = list(map(int,input().split()))

if sum(li) > n:
    print(-1)
else:
    print(n-sum(li))