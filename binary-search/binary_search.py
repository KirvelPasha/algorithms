def binarySearch(data, value):
    low = 0
    high = len(data) - 1
    mid = len(data) // 2

    while data[mid] != value and low <= high:
        if data[mid] < value:
            low = mid + 1
        else:
            high = mid - 1
        mid = (low + high) // 2

    if data[mid] == value:
        return mid
    else:
        return -1

def main():
    data = [1, 2, 3, 4, 5]
    value = int(input())
    print(binarySearch(data, value))

if __name__ == "__main__":
        main()


