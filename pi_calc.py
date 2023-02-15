# Calculates pi using Nilakantha, originally was doing Gregory Leibniz
import argparse
import math

def calc_pi(x):     # x = iterations
    approx = 0
    for i in range(x):
        sign = 4 if i % 2 == 0 else -4
        approx += (sign / (2 * i + 1))
        print("pi = {} error = {}".format(approx, math.pi - approx))
    print("native python pi: \npi = {}".format(math.pi))

parser = argparse.ArgumentParser(description="Approximates pi using Gregory-Leibniz series")
parser.add_argument("terms", help = "enter integer number of terms here", type = int)
args = parser.parse_args()

calc_pi(math.ceil(args.terms))

# unless i'm doing something wrong, Nilakantha's doesn't actually approach pi, must be python bit shift trickery under the hood
# despite oscillating calc_pi(n) > pi > calc_pi(n + 1), Leibniz at least gets closer in output