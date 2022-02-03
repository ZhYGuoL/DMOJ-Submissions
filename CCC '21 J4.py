shelf = input()

def get_count(shelf) -> list:
    count = [0, 0, 0]
    for book in shelf:
        if book == 'L':
            count[0] += 1
        elif book == 'M':
            count[1] += 1
        else:
            count[2] += 1
    return count


Lcount, Mcount, Scount = get_count(shelf)
print(get_count(shelf))

Lsection = get_count(shelf[:Lcount])
Msection = get_count(shelf[Lcount:Lcount+Mcount])
Ssection = get_count(shelf[Lcount+Mcount:])

single = min(Lsection[1], Msection[0]) + min(Lsection[2], Ssection[0]) + min(Msection[2], Ssection[1])