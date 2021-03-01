# https://atcoder.jp/contests/code-festival-2016-qualb/tasks/codefestival_2016_qualB_b

#a, b, m = map(int,input().split())
#a = list(map(int,input().split()))
#bc = 

n, a, b = map(int,input().split())
s = list(input())
x = 0 #予選通過人数
y = 0 #海外の人数

for c in s:
    if c == "a": 
        if x < a+b:
            x += 1
            print("Yes")
        else:
            print("No")
    if c == "b":
        if x < a+b and y < b:
            x += 1
            y += 1
            print("Yes")
        else:
            print("No")
    if c == "c":
        print("No")