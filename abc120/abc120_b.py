# https://atcoder.jp/contests/abc120/tasks/abc120_b

a, b, k = map(int,input().split())
 
def cf(x1,x2):
    cf=[]
    for i in range(1,min(x1,x2)+1):
        if x1 % i == 0 and x2 % i == 0:
            cf.append(i)
    return cf

ans = cf(a,b)
ans.sort(reverse=True)

print(ans[k-1])