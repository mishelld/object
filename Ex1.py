# import json
import csv
import sys
import subprocess
from Elevator import Elevator
from Building import Building
from CallForElevator import CallForElevator


building = Building('B5.json')
calls = []




def insertCalls(file):
    with open(file, 'r') as f:
        data = csv.reader(f)
        for call in data:
            calls.append(CallForElevator(call))

def algorithm(call):
#we will check which Elevator has the best speed
#and is free of calls, by using a for loop
#to compare the speeds of all the elevators until we find the best one
    max = 0
    max1 = 0
    for elev in building._elevators:
        if elev.getSpeed() > max and elev.iffree():
            max=elev.getSpeed()

#we will check which elevator has the optimal speed in comparison to the
#time of the elevator to get to the calls
    for elev in building._elevators:
        if elev.calculatspeed(call) > max1:
         max1 = elev.calculatspeed(call)

#if the the best elevator speed and the best elevator speed with time equals
#then we return it
    if max==max1:
        return max
#else if the speed of the elevator per time is bigger then the elevator speed
    elif max1>max :
        return max1
    else:
        return max





if __name__ == "__main__":
    insertCalls('Calls_a.csv')

