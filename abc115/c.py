# https://atcoder.jp/contests/abc115/tasks/abc115_c

n, k = map(int,input().split())
h =[int(input()) for i in range(n)]
h.sort()
ans = 1000000000000

for i in range(len(h)-k+1):
    if h[i+k-1] - h[i] < ans:
        ans = h[i+k-1] - h[i]
        if ans == 0:
            break

print(ans)