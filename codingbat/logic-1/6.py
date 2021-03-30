def alarm_clock(day, vacation):
    if (day == 0 or day == 6) and vacation == False:
        return '10:00'
    elif (day == 0 or day == 6) and vacation == True:
        return 'off'
    elif 1 <= day <= 5 and vacation == False:
        return '07:00'
    elif 1 <= day <= 5 and vacation == True:
        return '10:00'