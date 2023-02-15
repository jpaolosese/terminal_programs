# Trying my hand at cube roots to see if Newton's method works
import argparse
import math

def f(x, a):        # x^3 = a -> f(x) = x^3 - a
    return (x ** 3) - a

def f_prime(x):
    return 3 * (x ** 2) # f'(x) = 3x^2

def cube_root(x):     # Where x is the cube
    guess = 1
    for i in range(50):
        guess = guess - (f(guess, x) / f_prime(guess))  # Newton's method: x - f(x)/f'(x)
        print("iteration {}: {}. error = {}".format(i + 1, guess, guess - math.pow(x, 1/3)))
        if guess - math.pow(x, 1/3) <= 0 or guess - math.pow(x, 1/3) < 1e-15:
            break
    print("comparison : {}.  guess^3 = {}".format(math.pow(x, 1/3), (guess ** 3)))
    
        
parser = argparse.ArgumentParser(description="Calculates cube root using Newton/Babylonian iteration")
parser.add_argument("cube", help = "enter cube here", type = float)
args = parser.parse_args()

cube = args.cube
cube_root(cube)

# "If you are the head that floats atop the ziggurat, then the stairs that lead to you must be infinite. Infinite stairs are unacceptable."
# Doesn't work.