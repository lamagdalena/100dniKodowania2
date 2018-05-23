def slownik_kwadratow(n):
    keys = []
    values = []
    for x in range(1, n+1):
        keys.append(x)
        values.append(x * x)

    slownik = dict(zip(keys, values))

    return slownik

print(slownik_kwadratow(10))