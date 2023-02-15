# Calculates e with x iterations using (1 + 1/x) ^ x

import argparse
import math

def calculate_e(x):
    estimate = 1
    for i in range(x):
        estimate = (1 + (1 / x)) ** x
    print("e ~= {}".format(estimate))

parser = argparse.ArgumentParser(description="Calculates e constant in x iterations")
parser.add_argument("x", help = "how many iterations to calculate e to", type = int)
args = parser.parse_args()

calculate_e(args.x)