__author__ = 'skux'

#actually simplified version of Day 9, so far
import re
import sys
from itertools import permutations  #python <3


relationships = {}
names = set()
hapiness = 0


def parseLine(line):
    #will return triple, in order: 1st person, 2nd person, points
    #where first person gains or loses points for sitting next to person
    parsed = re.match(r'(.*) would (.*) (\d+) happiness units by sitting next to (.*)\.', line)
    if parsed.group(2) == 'gain':
        return parsed.group(1), parsed.group(4), int(parsed.group(3))
    else:
        return parsed.group(1), parsed.group(4), int(parsed.group(3)) * -1


def addYou():
    global names, relationships
    for name in names:
        relationships[(name, 'You')] = 0
        relationships[('You', name)] = 0
    names = list(names)
    names.append('You')


def storeInDict(line):
    global relationships
    spittedData = parseLine(line)
    #can make tuple, 'cause relationship is defined in both directions
    relationships[(spittedData[0], spittedData[1])] = spittedData[2]


#not necessary, but I'll add this one
def parseNames():
    global names, relationships
    names = [key[0] for key in relationships]
    names = set(names)


def main():
    global hapiness
    global names
    global relationships
    map(storeInDict, open(sys.argv[1]).readlines())
    parseNames()
    for combination in permutations(names):
        possible = 0
        for index in range(len(combination)):
            if index is not len(combination) - 1:
                possible = possible + int(relationships[(combination[index], combination[index + 1])]) + int(
                    relationships[(combination[index + 1], combination[index])])
            else:
                possible = possible + int(relationships[combination[index], combination[0]]) + int(
                    relationships[(combination[0], combination[index])])
        hapiness = max(hapiness, possible)
    print hapiness

    addYou()
    hapiness = 0
    print names
    print relationships
    for combination in permutations(names):
        possible = 0
        for index in range(len(combination)):
            if index is not len(combination) - 1:
                possible = possible + int(relationships[(combination[index], combination[index + 1])]) + int(
                    relationships[(combination[index + 1], combination[index])])
            else:
                possible = possible + int(relationships[combination[index], combination[0]]) + int(
                    relationships[(combination[0], combination[index])])
        hapiness = max(hapiness, possible)
    print hapiness


if __name__ == "__main__":
    main()