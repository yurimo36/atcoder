# https://atcoder.jp/contests/abc098/tasks/abc098_b

n = int(input())
s = input()
ans = 0

for i in range(1,n):
    x = ''.join(set(s[:i]))
    y = ''.join(set(s[i:]))
    z = 0
    for j in y:
        if j in x:
            z += 1
    if z > ans:
        ans = z
        
print(ans)