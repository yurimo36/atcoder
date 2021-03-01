# https://atcoder.jp/contests/abc131/tasks/abc131_c

import fractions

def lcm(x, y):
    return (x * y) // fractions.gcd(x, y)

a, b, c, d = map(int,input().split())
ans = 0
a = a-1
 
x = b - (b//c + b//d - b//lcm(c,d)) #1~bまでの該当する数
y = a - (a//c + a//d - a//lcm(c,d)) #1~a-1までの該当する数
    
print(x-y)