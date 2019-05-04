import sys
from functional_spec.src.ParkingLotImpl import ParkingLotImpl
from functional_spec.src.models.Car import *
from functional_spec.src.models.Commands import *

class ParkingLotHelper:
    def __init__(self):
        self.parkingLot = 0

    def operateCommand(self, line):
        try:
            content = line.split()
            command = content[0]
            cmd = getCommand(command)
            if Commands.CREATE.value == cmd:
                cnt = int(content[1])
                if self.parkingLot == 0:
                    self.parkingLot = ParkingLotImpl(cnt)
                else:
                    print("Parking Lot is already there")

                print("Created a parking lot with " + str(cnt) + " slots")
                return 1
            elif Commands.LEAVE.value == cmd:
                cnt = int(content[1])
                self.parkingLot.leaveCar(cnt - 1)
                print("Slot number " + str(cnt) + " is free")
                return 1
            elif Commands.PARK.value == cmd:
                regNo = content[1]
                colour = content[2]
                parkingres = self.parkingLot.parkCar(Car(regNo, colour))
                if parkingres != -1:
                    print("Allocated Slot Number: " + str(parkingres))
                else:
                    print("Sorry, parking lot is full")
                return 1
            elif Commands.REG_NUMBERS.value == cmd:
                colour = content[1]
                self.parkingLot.getRegNumberForColor(colour)
                return 1
            elif Commands.SLOT_COLOUR.value == cmd:
                colour = content[1]
                self.parkingLot.getSlotNumberForColor(colour)
                return 1
            elif Commands.SLOT_REG.value == cmd:
                regNo = content[1]
                parkingres = self.parkingLot.getSlotNumberForReqNumber(regNo)
                if parkingres != -1:
                    print(parkingres)
                else:
                    print("Not Found")
                return 1
            elif Commands.STATUS.value == cmd:
                self.parkingLot.getStatus()
                return 1
            else:
                return -1
        except:
            print("Oops!", sys.exc_info()[0], "occured.")

