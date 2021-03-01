# https://atcoder.jp/contests/arc021/tasks/arc021_1

#a, b, m = map(int,input().split())
#a = list(map(int,input().split()))
#bc = 

li = [input().split() for i in range(4)]
ans = 0

#横に同じ要素があるか見る
for l in li:
    for i in range(3):
        if l[i] == l[i+1]:
            ans = 1

#縦に同じ要素があるか見る
for i in range(4):
    for j in range(3):
        if li[j][i] == li[j+1][i]:
            ans = 1

if ans == 1:
    print("CONTINUE")
else:
    print("GAMEOVER")