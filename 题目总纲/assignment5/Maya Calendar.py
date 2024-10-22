i = int(input())
print(i)
months = ['pop', 'no', 'zip', 'zotz', 'tzec', 'xul', 'yoxkin', 'mol', 'chen', 'yax', 'zac', 'ceh', 'mac',
          'kankin', 'muan', 'pax', 'koyab', 'cumhu']
mons = ['imix', 'ik', 'akbal', 'kan', 'chicchan', 'cimi', 'manik', 'lamat', 'muluk', 'ok', 'chuen',
        'eb', 'ben', 'ix', 'mem', 'cib', 'caban', 'eznab', 'canac', 'ahau']
for _ in range(i):
    day, mon, year = input().split()
    d = int(day.strip('.'))
    year = int(year)
    if mon != 'uayet':
        n = d + months.index(mon)*20 + year*365 + 1
    else:
        n = d + year*365 + 361
    m = n % 20 - 1
    k = (n-1) % 13 + 1
    y = (n-1) // 260
    print(k, mons[m], y)
