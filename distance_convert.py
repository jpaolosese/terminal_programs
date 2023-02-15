import argparse

parser = argparse.ArgumentParser(description="converts meters to feet, unless specified")

group = parser.add_mutually_exclusive_group()
group.add_argument("-f", "--feet", help="converting from feet to meters", action="store_true")
group.add_argument("-m", "--meter", help="converting from meters to feet (default)", action="store_false")

group_2 = parser.add_mutually_exclusive_group()
group_2.add_argument("-v", "--verbose", action="store_true")
group_2.add_argument("-q", "--quiet", action="store_true")

parser.add_argument("distance", help="enter distance here. default converts from m to ft.", type=float)
args = parser.parse_args()

answer = args.distance * 3.28084

if args.feet == True:
    answer = args.distance * 0.304799

if args.quiet:
    print(answer)
elif args.verbose:
    if args.feet == True:
        print("{} ft converts to {} m".format(args.distance, answer))
    else:
        print("{} m converts to {} ft".format(args.distance, answer))
else:
    if args.feet == True:
        print("{} ft == {} m".format(args.distance, answer))
    else:
        print("{} m == {} ft".format(args.distance, answer))