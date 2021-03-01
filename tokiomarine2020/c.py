# https://atcoder.jp/contests/tokiomarine2020/tasks/tokiomarine2020_c

n, k = map(int,input().split())
li = list(map(int,input().split()))

for i in range(k):
    now = [0]*n

    for j in range(n):
        x = li[j]
        now[max(0,j-x)] += 1
        if j+x+1 < n:
            now[j+x+1] -= 1
    
    for j in range(n-1):
        now[j+1] += now[j]

    li = now
    if min(li) >= n:
        break

print(*li)
