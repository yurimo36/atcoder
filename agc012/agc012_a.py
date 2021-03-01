# https://atcoder.jp/contests/agc012/tasks/agc012_a

n = int(input())
li = list(map(int,input().split()))
li.sort(reverse=True)
print(sum(li[1:2*n:2]))