# https://atcoder.jp/contests/abc145/tasks/abc145_c

n = int(input())
li = []
ans = 0.0
x = 0

for i in range(n):
    li.append(list(map(int,input().split())))

for i in range(n-1):
    for j in range(i+1,n):
        ans += 2*(n-1)*(((li[i][0]-li[j][0])**2+(li[i][1]-li[j][1])**2))**0.5
        x += 1

print(ans/x/2)