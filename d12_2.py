__author__ = 'skux'

#I have no idea how to solve this one with regexes, unlike first part, so I'll import JSON

import sys
from json import loads


def parse(obj):
    if type(obj) is int:
        return obj

    if type(obj) is list:
        return sum(map(parse, obj))

    if type(obj) is dict:
        vals = obj.values()
        return 0 if "red" in vals else sum(map(parse, vals))
    #if all fails
    return 0


def main():
    print parse(loads(open(sys.argv[1]).read()))


if __name__ == "__main__":
    main()