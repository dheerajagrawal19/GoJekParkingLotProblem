Constants = {
    "CREATE" : "create_parking_lot",
    "PARK" : "park",
    "LEAVE" : "leave",
    "STATUS" : "status",
    "REG_NUMBERS" : "registration_numbers_for_cars_with_colour",
    "SLOT_COLOUR" : "slot_numbers_for_cars_with_colour",
    "SLOT_REG" : "slot_number_for_registration_number"
}

def getCommandKey(cmd):
    for i in Constants:
        if cmd == Constants[i]:
            return i

    return -1