# https://atcoder.jp/contests/abc137/tasks/abc137_b

k, x = map(int,input().split())

for i in range(x-k+1,x+k):
    print(i, end=' ')
print()