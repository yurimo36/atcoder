# https://atcoder.jp/contests/abc171/tasks/abc171_d

n = int(input())
li = list(map(int,input().split()))
y = [0]*10**5
for i in li:
    y[i-1] += 1
q = int(input())
bc = [list(map(int,input().split())) for i in range(q)]
x = sum(li)
#print(y)
for i in range(q):
    b = bc[i][0]
    c = bc[i][1]
    d = y[b-1]
    e = y[c-1]
    y[b-1] = 0
    y[c-1] = d+e
    x = x + (c-b) * d
    print(x)
    #print(y)