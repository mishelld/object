

class Elevator:

    def __init__(self, data):
        self._id = data["_id"]
        self._speed = data["_speed"]
        self._minFloor = data["_minFloor"]
        self._maxFloor = data["_maxFloor"]
        self._closeTime = data["_closeTime"]
        self._openTime = data["_openTime"]
        self._starTime = data["_startTime"]
        self._stopTime = data["_stopTime"]
        self._calls = []
        self._getposition = 0

    def getSpeed(self):
        return self._speed

    def iffree(self):
        if self._calls.__len__ == 0:
            return True
        else:
            return False

    def calculatspeed(self, call):
       src = abs(self._getposition - call.src)
       dest = abs(call.src - call.dest)
       dist = src + dest
       thetime = 0
       if src == 0:
           # the time for the elevtor to open the doors and then close them
           timesrc = self._openTime + self._closeTime
           # the time for the elevator to start moving on full speed and stoping and then
           # opening the dorrs in the dest
           timegotodest = self._starTime + self._stopTime + self._openTime
           thetime = timesrc + timegotodest
       elif src != 0:
           timetosrc = self._starTime + self._stopTime + self._openTime + self._closeTime
           timegotodest = self._starTime + self._stopTime + self._openTime
           thetime = timetosrc + timegotodest

       thespeed = dist / thetime
       return thespeed





    def __str__(self) -> str:
        print = "Elevator number: " + str(self._id) + "\n"
        print += "Speed: " + str(self._speed)
        print += " CloseTime: " + str(self._closeTime)
        print += " OpenTime: " + str(self._openTime)
        print += " StartTime: " + str(self._starTime)
        print += " StopTime: " + str(self._stopTime) + "\n"
        return print







