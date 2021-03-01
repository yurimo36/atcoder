# https://atcoder.jp/contests/cf16-final/tasks/codefestival_2016_final_a

h, w = map(int,input().split())
li = [input().split() for i in range(h)]

for i in range(h):
    for j in range(w):
        if li[i][j] == "snuke":
            print(chr(j+65)+str(i+1))
            exit()