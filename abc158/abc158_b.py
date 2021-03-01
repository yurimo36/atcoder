# https://atcoder.jp/contests/abc158/tasks/abc158_b

n, a, b = map(int,input().split())
 
x = int(n/(a+b)) #何周目か
y = n%(a+b) #余り

if y > a:
    ans = (x+1) * a
else:
    ans = x * a + y

print(ans)