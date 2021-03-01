# https://atcoder.jp/contests/indeednow-quala/tasks/indeednow_2015_quala_2

n = int(input())
li = [input() for i in range(n)]

for w in li:
    if w.count("i") == 1 and w.count("n") == 2 and w.count("d") == 2 and w.count("e") == 2 and w.count("o") == 1 and w.count("w") == 1:
        print("YES")
    else:
        print("NO")
