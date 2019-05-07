from __future__ import print_function


class ParkingLotImpl:
    def __init__(self, cap):
        self.capacity = cap
        self.availability = cap
        self.parkingLotMap = dict()
        self.freeSlots = []
        for i in range(cap):
            self.parkingLotMap[i] = 0
            self.freeSlots.append(i)

    def parkCar(self, car):
        if self.availability == 0:
            return -1

        nextAvail = self.freeSlots[0]
        self.parkingLotMap[nextAvail] = car
        self.availability = self.availability - 1
        self.freeSlots.remove(nextAvail)
        return nextAvail + 1

    def leaveCar(self, slotNum):
        self.availability = self.availability + 1
        self.freeSlots.append(slotNum)
        self.parkingLotMap[slotNum] = 0

    def getStatus(self):
        print("Slot No\tRegistration No\tColour")
        for i in range(self.capacity):
            r = self.parkingLotMap[i]
            if r != 0:
                print(str(i + 1) + "\t" + r.getRegNo() + "\t" + r.getColour())

    def getRegNumberForColor(self, colour):
        res = []
        for i in range(self.capacity):
            r = self.parkingLotMap[i]
            if r != 0 and r.getColour() == colour:
                res.append(r.getRegNo())

        self.printString(res)

    def getSlotNumberForColor(self, colour):
        res = []
        for i in range(self.capacity):
            r = self.parkingLotMap[i]
            if r != 0 and r.getColour() == colour:
                res.append(i + 1)

        self.printNumbers(res)

    def getSlotNumberForReqNumber(self, regNum):
        res = -1
        for i in range(self.capacity):
            r = self.parkingLotMap[i]
            if r != 0 and r.getRegNo() == regNum:
                res = i + 1

        return res

    def printNumbers(self, list):
        for i in range(len(list) - 1):
            print(str(list[i]) + ", ", end=' ')

        print(str(list[len(list) - 1]))

    def printString(self, list):
        for i in range(len(list) - 1):
            print(list[i] + ", ")

        print(list[len(list) - 1])
