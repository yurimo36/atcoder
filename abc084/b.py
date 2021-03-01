# https://atcoder.jp/contests/abc084/tasks/abc084_b

x,y = map(int,input().split())
s = input()

if len(s)==x+y+1 and s.count("-")==1 and s[:x].isdecimal() and s[x+1:].isdecimal():
    print("Yes")
else:
    print("No")