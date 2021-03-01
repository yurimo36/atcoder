# https://atcoder.jp/contests/abc167/tasks/abc167_d

n, k = map(int,input().split())
li = list(map(int,input().split()))
ans = [1]
nex = 1
f = [1]+[0]*(n-1)

for i in range(n):
    now = nex #今の場所
    nex = li[now-1] #テレポート先の場所
    #print(now,nex)
    if f[nex-1] == 1: #循環判定
        a = ans.index(nex) #開始点
        b = ans.index(now)-a+1 #循環周期
        break
    f[now-1] = 1
    ans.append(li[now-1])

#print(ans)
#print(f)
if k <= a:
    print(ans[k])
else:
    x = (k-a)%b
    print(ans[a+x])