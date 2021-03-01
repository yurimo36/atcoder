# https://atcoder.jp/contests/abc188/tasks/abc188_c

n = int(input())
li = list(map(int,input().split()))
l = len(li)//2

a = max(li[:l])
b = max(li[l:])
c = min(a, b)

print(li.index(c)+1)
