# https://atcoder.jp/contests/arc013/tasks/arc013_1

n, m, l = map(int,input().split())
p, q, r = map(int,input().split())
x = max(n,m,l)
y = max(p,q,r)

if x < y:
    #1個も入らない
    print(0)
else:
    #6通りの向きを全て試す
    a = (n//p) * (m//q) * (l//r)
    b = (n//p) * (m//r) * (l//q)
    c = (n//q) * (m//p) * (l//r)
    d = (n//q) * (m//r) * (l//p)
    e = (n//r) * (m//p) * (l//q)
    f = (n//r) * (m//q) * (l//p)
    print(max(a,b,c,d,e,f))