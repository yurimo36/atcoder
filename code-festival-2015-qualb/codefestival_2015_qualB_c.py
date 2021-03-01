# https://atcoder.jp/contests/code-festival-2015-qualb/tasks/codefestival_2015_qualB_c

x, y = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

if x < y:
    print("NO")
    exit()

a.sort(reverse=True)
b.sort(reverse=True)

for i in range(y):
    if a[i] < b[i]:
        print("NO")
        exit()
print("YES")