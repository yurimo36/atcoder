# https://atcoder.jp/contests/arc017/tasks/arc017_1

n = int(input())

for i in range(2,n-1):
    if n%i == 0:
        print("NO")
        exit()
    
print("YES")