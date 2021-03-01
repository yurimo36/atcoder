# https://atcoder.jp/contests/dwango2016-prelims/tasks/dwango2016qual_b

n = int(input())
li = list(map(int,input().split()))

ans = [li[0]]
for i in range(n-2):
    ans.append(min(li[i],li[i+1]))
ans.append(li[-1])

print(*ans)
