# https://atcoder.jp/contests/tenka1-2017-beginner/tasks/tenka1_2017_b

n = int(input())
li = [list(map(int,input().split())) for i in range(n)]
a = 0
b = 0

for i in li:
    if i[0] > a:
        a = i[0]
        b = i[1]

print(a+b)