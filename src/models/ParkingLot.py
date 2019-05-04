class ParkingLot:
    def __init__(self, slotNo, car):
        self.slotNo = slotNo
        self.car = car

    def getSlotNumber(self):
        return self.slotNo

    def getCar(self):
        return self.car