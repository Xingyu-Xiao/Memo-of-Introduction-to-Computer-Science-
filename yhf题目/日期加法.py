a = list(input().split('-'))
day = int(a[2])
month = int(a[1])
year = int(a[0])
add = int(input()) + day
while add > 0:
    if month == 2 and add > 28:
        if year % 4 == 0 and year % 100 != 0:
            if add > 29:
                add -= 29
                month += 1
            else:
                break
        else:
            add -= 28
            month += 1
    elif month in [1, 3, 5, 7, 8, 10, 12] and add > 31:
        add -= 31
        if month == 12:
            year += 1
            month = 1
        else:
            month += 1
    elif month in [4, 6, 9, 11] and add > 30:
        add -= 30
        month += 1
    else:
        break
if month < 10:
    month = '0' + str(month)
else:
    month = str(month)
if add < 10:
    day = '0' + str(add)
else:
    day = str(add)
days = [str(year), month, day]
print('-'.join(days))
