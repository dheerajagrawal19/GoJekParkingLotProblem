from enum import Enum

from functional_spec.src.constants.Constants import *


class Commands(Enum):
    CREATE = 1
    PARK = 2
    LEAVE = 3
    STATUS = 4
    REG_NUMBERS = 5
    SLOT_COLOUR = 6
    SLOT_REG = 7

    @staticmethod
    def get_list():
        return {i.name: i.value for i in Commands}


def getCommand(cmd):
    cmdKey = getCommandKey(cmd)
    if cmdKey != -1 :
        return Commands[cmdKey].value

    return -1
