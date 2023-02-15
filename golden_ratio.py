# Calculating the golden ratio phi, but in Python
# Converges to 1 + sqrt(5) / 2 at around 38th recursions

import argparse
import math

def fibonacci(x):       # where x is nth Fibonacci number
    if x <= 1:
        return x
    else:
        return fibonacci(x - 1) + fibonacci(x - 2)

parser = argparse.ArgumentParser(description="approximates phi to nth term")
parser.add_argument("term", help = "enter n recursions here", type = int)
args = parser.parse_args()

golden_ratio = (1 + math.sqrt(5)) / 2

print("phi ~= {}".format(fibonacci(args.term + 1) / fibonacci(args.term)))
print("Compare:\nphi == {}".format(golden_ratio))