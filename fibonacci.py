# Recreating the classic Fibonacci sequence, but in Python

import argparse
import math

def fibonacci(x):       # where x is nth Fibonacci number
    if x <= 1:
        return x
    else:
        return fibonacci(x - 1) + fibonacci(x - 2)

parser = argparse.ArgumentParser(description="Calculates xth Fibonacci number")
parser.add_argument("term", help = "enter x recursions here", type = int)
args = parser.parse_args()

print("Fibonacci sequence: ")
for i in range(args.term + 1):
    print(fibonacci(i))
