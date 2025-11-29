d1 = {'x': 10, 'y': 20}
d2 = {'y': 30, 'z': 40}

for key in d2:
    if key not in d1:
        d1[key] = d2[key]

print(d1)
