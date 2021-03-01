# https://atcoder.jp/contests/agc015/tasks/agc015_a

a, b, c = map(int,input().split())

x = b*(a-1)+c
y = c*(a-1)+b

print(max(0,y-x+1))