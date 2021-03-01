# https://atcoder.jp/contests/abc085/tasks/abc085_c

x, y = map(int,input().split())

for i in range(x+1):
    for j in range(x+1):
        z = 10000*i + 5000*j
        if y-z == 1000*(x-i-j) and x-i-j >= 0:
            print(i, j, x-i-j)
            exit()

print(-1, -1, -1)