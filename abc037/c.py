# https://atcoder.jp/contests/abc037/tasks/abc037_c

n, k = map(int,input().split())
li = list(map(int,input().split()))
ans = sum(li[:k])
x = ans
 
for i in range(1, n-k+1):
    x = x - li[i-1] + li[i+k-1]
    ans += x
    
print(ans)