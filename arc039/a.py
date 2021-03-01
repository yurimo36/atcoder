# https://atcoder.jp/contests/arc039/tasks/arc039_a

a, b = map(int,input().split())

#全部試す
c = (900 + a%100) - b #aの百の位を9
d = ((a//100)*100 + 90 + a%10) - b #bの十の位を9
e = (a - a%10 + 9) - b #aの一の位を9
f = a - (100 + b%100) #bの百の位を1
g = a - ((b//100)*100 + b%10) #bの十の位を0
h = a - (b-b%10) #bの一の位を0

print(max(c, d, e, f, g, h))