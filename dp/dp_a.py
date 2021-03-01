# https://atcoder.jp/contests/dp/tasks/dp_a

n = int(input())
h = list(map(int,input().split()))
ans = []

for i in range(n):
    if i == 0:
        ans.append(0)
    elif i == 1:
        ans.append(abs(h[1]-h[0]))
    else:
        ans.append(min(ans[-1]+abs(h[i]-h[i-1]),ans[-2]+abs(h[i]-h[i-2])))

print(ans[-1])
