import json
from Elevator import Elevator

class Building:
    
    def __init__(self, file):
        with open(file,'r') as f:
            data = json.load(f)
            self._minFloor = int(data["_minFloor"])
            self._maxFloor = int(data["_maxFloor"])
            self._elevators = []
            for elev in data["_elevators"]:
                self._elevators.append(Elevator(elev))    
    
    def __str__(self) -> str:
        print = "[" + str(self._minFloor) + ", " + str(self._maxFloor) + "]\n"
        for elev in self._elevators:
            print += elev.__str__()
        return print