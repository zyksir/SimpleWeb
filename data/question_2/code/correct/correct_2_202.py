def unique_day(day, possible_birthdays):
    new = ()
    for i in range (len(possible_birthdays)):
        new = new + (possible_birthdays[i][1],)
    if new.count(day) == 1:
        return True
    else:
        return False

def unique_month(month, possible_birthdays):
    new = ()
    for i in range (len(possible_birthdays)):
        new = new + (possible_birthdays[i][0],)
    if new.count(month) == 1:
        return True
    else:
        return False


def contains_unique_day(month, possible_birthdays):
    new = ()
    for i in possible_birthdays:
        if i[0] == month:
            new = new + (i[1],)
    for i in new:
        if unique_day(i, possible_birthdays):
            return True
    return False
