# https://atcoder.jp/contests/abc123/tasks/abc123_b

n = [int(input()) for i in range(5)]
m = 10
x = n[0]
#1の位が最も小さいものはそのまま足す・残りは1の位を切り上げて足す

for i in n:
  if int(str(i)[-1]) < m and int(str(i)[-1]) > 0:
    m = int(str(i)[-1])
    x = i



n.remove(x)
    
for i in range(len(n)):
  if n[i]%10 != 0:
    n[i] = n[i] + 10 - int(str(n[i])[-1])

print(sum(n) + x)