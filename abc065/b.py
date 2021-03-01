# https://atcoder.jp/contests/abc065/tasks/abc065_b

n = int(input())
a = [int(input()) for i in range(n)] #ボタンの仕様
x = [1] #遷移
 
for i in range(n):
    y = x[-1] #今の場所
    z = a[y-1]
    x.append(z)
    if z == 2:
        print(len(x)-1)
        exit()

print(-1)