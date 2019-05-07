import sys

from ParkingLotHelper import ParkingLotHelper

if __name__ == '__main__':
    plh = ParkingLotHelper()
    if len(sys.argv) > 1:
        try:
            file_name = sys.argv[1]  # "../test/input_file.txt"
            with open(file_name, "rb") as f:  # , encoding='utf-8
                for line in f:
                    plh.operateCommand(line)
        except Exception as e:
            type, value, traceback = sys.exc_info()
            print(type, value, traceback)
    else:
        try:
            while True:
                inp = raw_input()
                cmd = inp.strip()
                if plh.operateCommand(cmd) == -1:
                    break
        except Exception as e:
            type, value, traceback = sys.exc_info()
            print(type, value, traceback)
