def gcd(first, second):
    while first != second:
        if first > second:
            first -= second
        else:
            second -= first
    return first


def main():
    first = int(input("First:"))
    second = int(input("Second:"))
    print(gcd(first, second))


if __name__ == "__main__":
    main()
