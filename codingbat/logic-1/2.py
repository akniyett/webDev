def date_fashion(you, date):
    
    if 0 <= you or date <= 2:
        return 0
    elif 8 <= you or date <= 10:
        return 2
    else:
        return 1
