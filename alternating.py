# just want to see if i can get oscillating -1 and 1
import argparse

def alternating(x):
    for i in range(x):
        print(1 if i % 2 == 0 else -1)

parser = argparse.ArgumentParser(description="just seeing of I can get alternating -1 and 1")
parser.add_argument("terms", help = "enter number of terms here", type = int)
args = parser.parse_args()

alternating(args.terms)