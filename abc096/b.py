# https://atcoder.jp/contests/abc096/tasks/abc096_b

li = list(map(int,input().split()))
k = int(input())

for i in range(k):
    li.sort(reverse=True)
    li[0] = li[0] * 2

print(sum(li))