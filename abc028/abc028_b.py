# https://atcoder.jp/contests/abc028/tasks/abc028_b

s = input()
li = []
li.append(s.count("A"))
li.append(s.count("B"))
li.append(s.count("C"))
li.append(s.count("D"))
li.append(s.count("E"))
li.append(s.count("F"))
print(*li)