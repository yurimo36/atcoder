# https://atcoder.jp/contests/abc181/tasks/abc181_b

def wa(n):
    return n*(n+1)//2

n = int(input())
li = [list(map(int,input().split())) for i in range(n)]
ans = 0

for l in li:
    ans += wa(l[1])
    ans -= wa(l[0]-1)

print(ans)
