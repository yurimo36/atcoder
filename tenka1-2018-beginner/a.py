# https://atcoder.jp/contests/tenka1-2018-beginner/tasks/tenka1_2018_a

s = input()

if len(s)%2 == 0:
    print(s)
else:
    print(s[::-1])