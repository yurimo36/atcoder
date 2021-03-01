# https://atcoder.jp/contests/abc114/tasks/abc114_c

n = int(input())
l = [3, 5, 7]
ans = 0

for i in range(26484):
    x = str(l[i])
    l.append(int(x+"3"))
    l.append(int(x+"5"))
    l.append(int(x+"7"))

for i in l:
    if i > n:
        print(ans)
        break
    
    x = str(i)
    if x.count("3")>0 and x.count("5")>0 and x.count("7")>0:
        ans += 1