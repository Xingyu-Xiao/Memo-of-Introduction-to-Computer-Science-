def length_of_longest_substring(s):
    n = len(s)
    max_len = 0
    se = set()
    j = 0
    for i in range(n):
        while j < n:
            if s[j] in se:
                break
            else:
                se.add(s[j])
                j += 1
        max_len = max(max_len, j-i)
        se.difference_update((s[i]))
    return max_len


