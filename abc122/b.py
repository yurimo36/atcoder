# https://atcoder.jp/contests/abc122/tasks/abc122_b

s = input()
ans = 0

if len(s)==1:
    if s.count("A")+s.count("G")+s.count("C")+s.count("T") == 1:
        print(1)
        exit()

 
for i in range(len(s)-1):
    for j in range(i+1, len(s)+1):
        x = s[i:j]
        if x.count("A")+x.count("G")+x.count("C")+x.count("T") == len(x) and len(x) > ans:
            ans = len(x)
 
print(ans)