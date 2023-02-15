import argparse

parser = argparse.ArgumentParser(description="converts Celsius to Fahrenheit, unless specified")

group = parser.add_mutually_exclusive_group()
group.add_argument("-f", "--fahrenheit", help="converting from F to C ", action="store_true")
group.add_argument("-c", "--celsius", help="converting from C to F. (default)", action="store_false")

group_2 = parser.add_mutually_exclusive_group()
group_2.add_argument("-v", "--verbose", action="store_true")
group_2.add_argument("-q", "--quiet", action="store_true")

parser.add_argument("temperature", help="enter temperature here. default converts from C to F", type=float)
args = parser.parse_args()

answer = (args.temperature * 1.8) + 32

if args.fahrenheit == True:
    answer = (args.temperature - 32)/1.8

if args.quiet:
    print(answer)
elif args.verbose:
    if args.fahrenheit == True:
        print("{} F converts to {} C".format(args.temperature, answer))
    else:
        print("{} C converts to {} F".format(args.temperature, answer))
else:
    if args.fahrenheit == True:
        print("{} F == {} C".format(args.temperature, answer))
    else:
        print("{} C == {} F".format(args.temperature, answer))