from datetime import datetime
def dayOfProgrammer(year):
    if year < 1918:
        if year%4 == 0:
            day  = 256 - (31 + 29 + 31 + 30 + 31 + 30 + 31 + 31)
        else:
            day  = 256 - (31 + 28 + 31 + 30 + 31 + 30 + 31 + 31)
    elif year == 1918:
        if year % 400 == 0:
            day  = 256 - (31 + 29 + 31 + 30 + 31 + 30 + 31 + 31)+13
        else:
            if year % 4 == 0 and year % 100 != 0:
                day  = 256 - (31 + 29 + 31 + 30 + 31 + 30 + 31 + 31)+13
            else:
                day  = 256 - (31 + 28 + 31 + 30 + 31 + 30 + 31 + 31)+13
    else:
        if year % 400 == 0:
            day  = 256 - (31 + 29 + 31 + 30 + 31 + 30 + 31 + 31)
        else:
            if year % 4 == 0 and year % 100 != 0:
                day  = 256 - (31 + 29 + 31 + 30 + 31 + 30 + 31 + 31)
            else:
                day  = 256 - (31 + 28 + 31 + 30 + 31 + 30 + 31 + 31)

    return str(day)+".09."+str(year)

if __name__ == "__main__":

    print(dayOfProgrammer(1918))