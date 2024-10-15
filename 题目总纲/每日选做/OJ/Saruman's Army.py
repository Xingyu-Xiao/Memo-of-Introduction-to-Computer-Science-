while True:
    R, n = map(int, input().split())
    if R == n == -1:
        break
    locations = list(map(int, input().split()))
    if n != 1:
        locations.sort()
        i = 1
        location = locations[0]
        out = 0
        while True:
            p = False
            while True:
                if locations[i] - location <= R:
                    i += 1
                    if i == n:
                        out += 1
                        break
                else:
                    if p:
                        out += 1
                        location = locations[i]
                        i += 1
                        if i == n:
                            out += 1
                        break
                    else:
                        p = True
                        location = locations[i-1]
            if i == n:
                break
        print(out)
    else:
        print(1)
