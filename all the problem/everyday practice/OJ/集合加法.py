n = int(input())
for _ in range(n):
    s = int(input())
    a = int(input())
    A = list(map(int, input().split()))
    b = int(input())
    B = list(map(lambda x: s-int(x), input().split()))
    '''
    A.sort()
    B.sort()
    k = i = j = 0
    while i < a and j < b:
        if A[i] == B[j]:
            num_a = 1
            num_b = 1
            for x in A[i+1:]:
                if x == A[i]:
                    num_a += 1
                else:
                    break
            for y in B[j+1:]:
                if y == B[j]:
                    num_b += 1
                else:
                    break
            k += num_a * num_b
            i += num_a
            j += num_b
        elif A[i] < B[j]:
            i += 1
        elif A[i] > B[j]:
            j += 1
    print(k)
'''
#排序复杂度高
    count_A = {}
    for x in A:
        if x not in count_A:
            count_A[x] = 1
        else:
            count_A[x] += 1
    num = 0
    for y in B:
        if y in count_A:
            num += count_A[y]
    print(num)
