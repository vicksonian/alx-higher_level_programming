#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    argc = len(argv) - 1
    args = argv[1:]

    if argc == 0:
        print("0 arguments.")
    else:
        plural_s = "s" if argc > 1 else ""
        print("{} argument{}:".format(argc, plural_s))

        for i, arg in enumerate(args, 1):
            print("{}: {}".format(i, arg))
