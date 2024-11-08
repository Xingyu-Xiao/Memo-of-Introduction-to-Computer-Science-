y = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u', 'y', 'Y']
print('.'+'.'.join([x.lower() for x in input() if x not in y]))
