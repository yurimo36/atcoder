# https://atcoder.jp/contests/arc036/tasks/arc036_a

n, k = map(int,input().split())
li = [int(input()) for i in range(n)]
ans = 0
#print(li)

for i in range(n-2):
    if i == 0:
        s = sum(li[:3])
    else:
        s = s - li[i-1] + li[i+2]
    #print(i, s)
    if s < k:
        print(i+3)
        exit()

print(-1)