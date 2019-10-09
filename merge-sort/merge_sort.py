import random

def merge(data):
    n = len(data)
    if n < 2:
        return data

    l = merge(data[:n // 2])
    r = merge(data[n // 2:])
    i = j = 0
    res = []

    while i < len(l) or j < len(r):
        if not i < len(l):
            res.append(r[j])
            j += 1
        elif not j < len(r):
            res.append(l[i])
            i += 1
        elif l[i] < r[j]:
            res.append(l[i])
            i += 1
        else:
            res.append(r[j])
            j += 1
    return res



def main():
    data = [random.randrange(-10, 10) for i in range(10)]
    print(data)
    res = merge(data)
    print(res)

if __name__ == "__main__":
    main()