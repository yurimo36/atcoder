# https://atcoder.jp/contests/abc160/tasks/abc160_b

x = int(input())

print(int(x/500) * 1000 + int(int(x%500)/5) *5)