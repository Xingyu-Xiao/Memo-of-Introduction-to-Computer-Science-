while 1:
    n = int(input())
    if not n:
        break
    tian = list(map(int, input().split()))
    kings = list(map(int, input().split()))
    kings.sort()
    tian.sort()
    i = j = 0
    k = m = n-1
    ans = 0
    while i <= k:
        if tian[i] > kings[j]:
            ans += 200
            i += 1
            j += 1
        elif tian[k] > kings[m]:
            ans += 200
            k -= 1
            m -= 1
        else:
            if tian[i] < kings[m]:
                ans -= 200
            i += 1
            m -= 1
    print(ans)
