# https://atcoder.jp/contests/abc131/tasks/abc131_d

n = int(input())
li = []
x = 0

for i in range(n):
    li.append(list(map(int,input().split())))
li.sort(key=lambda x: x[1])

for i in range(n):
    x += li[i][0]
    if x > li[i][1]:
        print("No")
        exit()

print("Yes")