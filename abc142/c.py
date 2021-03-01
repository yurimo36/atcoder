# https://atcoder.jp/contests/abc142/tasks/abc142_c

n = int(input())
a = list(map(int,input().split()))
b = [0 for j in range(n)]

for i in range(n):
    b[a[i]-1] = i+1

print(*b)