# https://atcoder.jp/contests/abc054/tasks/abc054_b

x, y = map(int,input().split())
a = []
b = []

for i in range(x):
    a.append(list(input()))
for i in range(y):
    b.append(list(input()))

for i in range(x-y+1): #Aの中縦移動
    for j in range(x-y+1): #Aの中横移動→位置確定
        flag = 1
        for k in range(y): #bの全ての行
            if b[k] != a[i+k][j:j+y]:
                flag = 0
                break
        if flag == 1:
            print("Yes")
            exit()
print("No")