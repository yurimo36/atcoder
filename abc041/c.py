# https://atcoder.jp/contests/abc041/tasks/abc041_c

n = int(input())
li = list(map(int,input().split()))
for i in range(n):
    li[i] = [li[i], i+1]
ans = sorted(li, reverse=True)

for i in ans:
    print(i[1])