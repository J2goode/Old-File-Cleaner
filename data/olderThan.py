def olderThan(new, olderThan):
    """This program checks if one date is older than another. Returns True if older, False if not.
       Requires two dates: the first is the user input date, the second is the comparison date.
       BOTH DATES NEED TO BE STRINGS AND IN mm/dd/yyyy FORMAT"""
    from datetime import datetime
    from datetime import date

    n = str(date.today())

    now = str(n[5:7] + '/' + n[8:10] + '/' + n[:4])
    
    if olderThan == '':
        t2 = datetime.strptime(now, '%m/%d/%Y').date()
    else:
        t2 = datetime.strptime(olderThan, '%m/%d/%Y').date()
    
    t1 = datetime.strptime(new, '%m/%d/%Y').date()

    if t1 < t2:
        return True
    else:
        return False
