# Calculates e using factorial method
# Converges to e in 18 iterations

import argparse
import math

def calculate_e(x) :
    estimate = 0
    for i in range(x) :
        estimate += (1 / math.factorial(i))
        print("e ~= {}. Error = {}".format(estimate, math.e - estimate))
        if math.e - estimate < -1e-16:
            break
    print("Comparison with math module\ne == {}".format(math.e))
    return estimate

parser = argparse.ArgumentParser(description="Calculates e constant in x iterations")
parser.add_argument("x", help = "how many iterations to calculate e to", type = int)
args = parser.parse_args()

calculate_e(args.x)