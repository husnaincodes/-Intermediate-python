d = {'a': 1, 'b': 2, 'c': 3}

for k in d:
    if d[k] % 2 != 0:
        d[k] += 5
    else:
        d[k] *= 2

print(d)
