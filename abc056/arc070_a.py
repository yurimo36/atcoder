# https://atcoder.jp/contests/abc056/tasks/arc070_a

x = int(input())

for i in range(int(x**0.5),x+1):
    y = i*(i+1)//2
    if y >= x:
        print(i)
        exit()