import sys
from functional_spec.src.ParkingLotHelper import ParkingLotHelper

if __name__ == '__main__':
    plh = ParkingLotHelper()
    if len(sys.argv) > 1 :
        try:
            file_name = sys.argv[1] ##"../test/input_file.txt"
            with open(file_name, "r",encoding='utf-8') as f:
                for line in f:
                    plh.operateCommand(line)
        except IOError:
            print("IO Error Occured")
        except:
            print("Oops!", sys.exc_info()[0], "Occured.")
    else:
        while True:
            cmd = input()
            if plh.operateCommand(cmd) == -1:
                break

