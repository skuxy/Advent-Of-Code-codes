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
        self.Moved = 0
        self.Rested = 0
        self.Moving = True
        self.TotalMoved = 0  #in seconds


#returns reindeer object
def parseInput(line):
    data = re.match(r'(.*) can fly (\d+) km\/s for (\d+) seconds, but then must rest for (\d+) seconds.', line)
    return Reindeer(data.group(1), int(data.group(2)), int(data.group(3)), int(data.group(4)))


def printResults(reindeer):
    print "Reindeer " + reindeer.name + " traveled " + str(reindeer.TotalMoved * reindeer.speed)


def main():
    reindeers = list(map(parseInput, open(sys.argv[1]).readlines()))

    for sec in range(1):  #2503 seconds, tested with 1000 for given task and it's OK
        for reindeer in reindeers:
            if reindeer.Moving:
                if reindeer.Moved == reindeer.timeMoving:
                    reindeer.Moving = False
                    reindeer.Moved = 0
                    reindeer.Rested = 0
                else:
                    reindeer.Moved = reindeer.Moved + 1
                    reindeer.TotalMoved = reindeer.TotalMoved + 1
            else:
                if reindeer.Rested == reindeer.timeResting:
                    reindeer.Moving = True
                    reindeer.Moved = 0
                    reindeer.Rested = 0
                else:
                    reindeer.Rested = reindeer.Rested + 1

    map(printResults, reindeers)


if __name__ == "__main__":
    main()