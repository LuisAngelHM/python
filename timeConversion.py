def _12hrsTo24hors(time):
    period = time[-2:]
    hour = time[:2]
    if period == "PM" and hour != "12":
        hour=int(hour) + 12
    elif period == "AM" and hour == "12":
        hour="00"
    hour = str(hour) 
    return hour+time[2:-2]

if __name__ == "__main__":
    time="12:40:22AM"
    print("La hora en formato de 24 horas es: {}".format(_12hrsTo24hors(time)))