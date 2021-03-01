# https://atcoder.jp/contests/abc014/tasks/abc014_3

n = int(input())
li = [0]*1000001

for i in range(n):
    a, b = map(int,input().split())
    li[a] += 1
    if b < 1000000:
        li[b+1] -= 1

for i in range(1000000):
    li[i+1] += li[i]

print(max(li))