# https://atcoder.jp/contests/abc022/tasks/abc022_b

n = int(input())
a = [int(input()) for i in range(n)]
l = [0]*(10**5)

for i in a:
    l[i-1] += 1
 
print(sum(l)-len(l)+l.count(0))