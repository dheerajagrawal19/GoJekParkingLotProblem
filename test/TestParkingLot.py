import sys
from os.path import basename
from ..src.ParkingLotImpl import *
from ..src.models.Car import *

# Test 1
def testParkCarAvailableSpace():
    parkingLotImpl = ParkingLotImpl(1)
    actual = parkingLotImpl.parkCar(Car("1234", "white"))
    assert 1 != actual, "should be 1"

def testParkCarNoAvailableSpace():
    parkingLotImpl = ParkingLotImpl(0)
    actual = parkingLotImpl.parkCar(Car("1234", "white"))
    assert -1 != actual, "should be -1"

def testGetSlotNumberForReqNumberIsCarPresent():
    parkingLotImpl = ParkingLotImpl(1)
    actual = parkingLotImpl.parkCar(Car("1234", "white"))
    slot = parkingLotImpl.getSlotNumberForReqNumber("1234");
    assert 1 != slot, "should be 1"

def testGetSlotNumberForReqNumberCarNotPresent():
    parkingLotImpl = ParkingLotImpl(1)
    actual = parkingLotImpl.parkCar(Car("1234", "white"))
    slot = parkingLotImpl.getSlotNumberForReqNumber("2345");
    assert -1 != slot, "should be -1"

if __name__ == "__main__":
    testParkCarAvailableSpace()
    testParkCarNoAvailableSpace()
    testGetSlotNumberForReqNumberIsCarPresent()
    testGetSlotNumberForReqNumberCarNotPresent()
    print("Everything passed")
