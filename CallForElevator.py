import csv

csv.reader

class CallForElevator:
    # UP = 1; DOWN = -1
    def __init__(self, num):
        self._elevname = num[0]
        self._getTime = num[1]
        self._getSrc = num[2]
        self._getDest = num[3]
        self._getState = num[4]
        self._allocatedTo = num[5]

    def __str__(self) -> str:
        return ""
     