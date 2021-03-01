# https://atcoder.jp/contests/abc016/tasks/abc016_3

n, m = map(int,input().split())
p = [list(map(int,input().split())) for i in range(m)]
l = [[] for i in range(n)]
ans = [[] for i in range(n)]

for pi in p:  #0-originedに注意
    l[pi[0]-1].append(pi[1])
    l[pi[1]-1].append(pi[0])

for i in range(n): #i番目の人の友達の友達の人数を考える・l[i]がiの友達
    for j in range(n): 
        if i==j: #見てるものが自分自身だったら
            continue #skip
        for k in l[i]: #i番目の友達リストを見る
            if l[j].count(k) > 0:
                ans[i].append(j+1)

for i in range(n):
    ans[i] = list(set(ans[i]))
    for j in l[i]:
        if ans[i].count(j) > 0:
            ans[i].remove(j)
    print(len(ans[i]))