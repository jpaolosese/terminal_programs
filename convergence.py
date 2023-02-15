# 9.9999999999... = 10

import math

def series():
    partial = 0
    for i in range(150):
        partial += 9 / (10 ** i)
    return partial

print(series())