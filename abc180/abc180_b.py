# https://atcoder.jp/contests/abc180/tasks/abc180_b

n = int(input())
x = list(map(int,input().split()))
a = 0
b = 0.0
c = 0

for i in x:
    a += abs(i)
    b += i**2
    if abs(i) > c:
        c = abs(i)

print(a)
print(b**0.5)
print(c)
