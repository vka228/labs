def redar(file):
    res = ([])
    with open(file) as f:
        while True:
            line = float(f.readline())
            res.append((line))
            if not line:
                break
    return res[:len(res) - 1]

print(redar('test.txt'))
