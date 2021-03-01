# https://atcoder.jp/contests/abc079/tasks/abc079_c

import copy
import numpy as np

s = input()
n = 3
ans = 0

for i in range(1,3 ** n):
    x = copy.deepcopy(s)
    y = str(np.base_repr(i,3)).rjust(3,'0') #3進数に変換
    if (y[0] == "0" and s[0] == "0") or (y[1] == "0" and s[1] == "0") or (y[2] == "0" and s[2] == "0"):
        continue
    z = 1
    for j in range(3):
        if y[j] == "1": #フラグが立っていたら
            x = x[:j+z] + "+" + x[j+z:]
            z += 1
        if y[j] == "2": #フラグが立っていたら
            x = x[:j+z] + "-" + x[j+z:]
            z += 1
    if eval(x) == 7:
        print(x +"=7")
        exit()