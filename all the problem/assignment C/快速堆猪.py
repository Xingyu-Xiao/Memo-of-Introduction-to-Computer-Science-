min_pig = []
pig = []
while True:
    try:
        s = input()
        if s[0] == 'p':
            if s[1] == 'u':
                top = int(s.split()[1])
                pig.append(top)
                if min_pig:
                    min_pig.append(min(top, min_pig[-1]))
                else:
                    min_pig.append(top)
            if s[1] == 'o':
                if pig:
                    p = pig.pop()
                    if min_pig:
                        min_pig.pop()
        if s[0] == 'm':
            if min_pig:
                print(min_pig[-1])
    except EOFError:
        break
