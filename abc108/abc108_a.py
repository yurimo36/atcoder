# https://atcoder.jp/contests/abc108/tasks/abc108_a

k = int(input())

if k%2 == 1:
    print((k//2)*(k-k//2))
else:
    print((k//2)**2)