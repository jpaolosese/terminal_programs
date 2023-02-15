import argparse

parser = argparse.ArgumentParser(description="converts kilogram to pound, unless specified")

group = parser.add_mutually_exclusive_group()
group.add_argument("-p", "--pound", help="converting from pound to kilogram", action="store_true")
group.add_argument("-k", "--kilo", help="converting from kilogram to pound (default)", action="store_false")

group_2 = parser.add_mutually_exclusive_group()
group_2.add_argument("-v", "--verbose", action="store_true")
group_2.add_argument("-q", "--quiet", action="store_true")

parser.add_argument("mass", help="enter mass here. default converts from kg to lb.", type=float)
args = parser.parse_args()

answer = args.mass * 2.20462

if args.pound == True:
    answer = args.mass * 0.453592

if args.quiet:
    print(answer)
elif args.verbose:
    if args.pound == True:
        print("{} lb converts to {} kg".format(args.mass, answer))
    else:
        print("{} kg converts to {} lb".format(args.mass, answer))
else:
    if args.pound == True:
        print("{} lb == {} kg".format(args.mass, answer))
    else:
        print("{} kg == {} lb".format(args.mass, answer))