# Program computes square roots using Newton's Method
import argparse
import math

def square_root(x):     # Where x is the square
    guess = 1
    for i in range(50):    # Due to Python and software quirks, a method like this would loop infinitely with certain values
        guess = (guess + (x / guess)) / 2       # Newton's/Bablyonian method
        print("Square root of {} = {}. Error = {}".format(x, guess, (guess-math.sqrt(x))))
        if guess <= math.sqrt(x):
            break       
    print("Comparison with math module: \nSquare root of {} = {}. guess^2 = {}".format(x, math.sqrt(x), guess ** 2))
        
parser = argparse.ArgumentParser(description="Calculates square root using Newton/Babylonian iteration")
parser.add_argument("square", help = "enter square here", type = float)
args = parser.parse_args()

square_root(args.square)
if args.square == 912.04 or args.square == 906.01:
    print("It all seemed harmless...")
