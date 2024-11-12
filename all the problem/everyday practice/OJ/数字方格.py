n = int(input())


def f(n):
    for total in range(3*n, -1, -1):
        if total % 5 == 0:
            for a_1 in range(0, n+1):
                if (total-a_1) % 3 == 0:
                    for a_2 in range(0, n+1):
                        if (a_1+a_2) % 2 == 0 and (total - a_1 - a_2) in range(0, n+1):
                            return total


print(f(n))
