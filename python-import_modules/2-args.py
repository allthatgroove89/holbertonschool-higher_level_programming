#!/usr/bin/python3
import sys


def main():
    args = sys.argv[1:]
    if not args:
        not_arg_word = "arguments"
        print(str(len(args)) + ' ' + not_arg_word + ".")
    else:
        arg_word = "argument" if len(args) == 1 else "arguments"
        print(str(len(args)) + ' ' + arg_word + ":")
        for i, arg in enumerate(args, start=1):
            print(str(i) + ":", arg)


if __name__ == "__main__":
    main()
