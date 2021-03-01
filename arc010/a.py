# https://atcoder.jp/contests/arc010/tasks/arc010_1

n, m, a, b = map(int,input().split())
li = [int(input()) for i in range(m)]

for i in range(m):
    if n <= a:
        n += b
    n -= li[i]
    if n < 0:
        print(i+1)
        exit()
    
print("complete")