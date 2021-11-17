
class CallForElevator:

    # Cunstractur for the calls of the elevator.
    # the cunstractur recives from the csv file the objects:
    # name of the call, time of the call,the Src floor of the call,the dest floor of the call
    # the state of the call,which elevator the call is allocated to.

    INIT = 0; DONE = 3

    def __init__(self, data):
        self._name = data[0]
        self._time = float(data[1])
        self._src = int(data[2])
        self._dest = int(data[3])
        self._state = int(data[4])
        self._allocatedTo = int(data[5])
        self._finishedTime = -1

    # print the objects of the call
    def __str__(self):
        print = self._name + ": "
        print += "at " + str(self._time)
        print += " from " + str(self._src)
        print += " to " + str(self._dest)
        if self._state == self.INIT:
            print += " waiting for " + str(self._allocatedTo)
        elif self._state == self.DONE:
            print += " is Done!"
        else:
            print += " allocatedTo: " + str(self._allocatedTo)
        return print

    #a function that sets the current state of the call, which is if its done or not
    def setState(self, state):
        if not (state == self.INIT or state == self.DONE):
            raise Exception("ERROR: trying to set unvalid state to: \n" + self.__str__())
        self._state = state

    #a function that sets to which elevator to allocate the call
    def setAllocatedTo(self, elevator, building):
        isThere = False
        for elev in building.getElevators():
            if elevator.getId() == elev.getId() :
                isThere = True
        if not isThere:
            raise Exception("ERROR: trying to set unvalid elevator to: \n" + self.__str__())
        self._allocatedTo = elevator.getId()

    #a function that returns the time when a call is finished
    def setFinishedTime(self, time):
        self._finishedTime = time

    # a function that retruns the time of the call
    def getTime(self):
       return  self._time 

    # a functoin that returns the src floor of the call
    def getSrc(self):
       return  self._src

    # a functio  that returns the dest floor of the call
    def getDest(self):
       return  self._dest  

    #a funciton that returns the state of the call, if its done or not    
    def getState(self):
        return self._state

    # a function that returns to which eleavtor the call was allocated to
    def getAllocatedTo(self):
        return self._allocatedTo
        
    # a function that returns the finished time for the call
    def getFinishedTime(self):
        return self._finishedTime