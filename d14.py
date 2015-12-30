__author__ = 'skux'


#lots of redundant code in here, was too lazy, Sorry. At least I think it's straightforward

#NOTE: There IS input for this day :) Oops

import re
import sys


class Reindeer:
    def __init__(self, name, speed, timeMoving, timeResting):
        self.name = name
        self.speed = speed
        self.timeMoving = timeMoving  #const
        self.timeResting = timeResting  #const
        self.moved = 0
        self.rested = 0
        self.moving = True
        self.totalMoved = 0  #in seconds


#returns reindeer object
def parseInput(line):
    data = re.match(r'(.*) can fly (\d+) km\/s for (\d+) seconds, but then must rest for (\d+) seconds.', line)
    return Reindeer(data.group(1), int(data.group(2)), int(data.group(3)), int(data.group(4)))


def printResults(reindeer):
    print "Reindeer " + reindeer.name + " traveled " + str(reindeer.totalMoved * reindeer.speed)


def main():
    reindeers = list(map(parseInput, open(sys.argv[1]).readlines()))

    for sec in range(2503):  #2503 seconds, tested with 1000 for given task and it's OK. DISCLAIMER: NO IT IS NOT
        for reindeer in reindeers:
            if reindeer.moving:
                if reindeer.moved >= reindeer.timeMoving:
                    reindeer.moving = False
                    reindeer.moved = 0
                    reindeer.rested = 1
                else:
                    reindeer.moved = reindeer.moved + 1
                    reindeer.totalMoved = reindeer.totalMoved + 1
            else:
                if reindeer.rested >= reindeer.timeResting:
                    reindeer.moving = True
                    reindeer.moved = 1
                    reindeer.totalMoved = reindeer.totalMoved + 1
                    reindeer.rested = 0
                else:
                    reindeer.rested = reindeer.rested + 1

    map(printResults, reindeers)


if __name__ == "__main__":
    main()