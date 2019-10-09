import random

def quicksort(data):
    if len(data) <= 1:
        return data
    pivot = data[len(data) // 2]
    lef = [x for x in data if x < pivot]
    mid = [x for x in data if x == pivot]
    right = [x for x in data if x > pivot]
    return quicksort(lef) + mid + quicksort(right)

def main():
    data = [random.randrange(-10, 10) for i in range(10)]
    print(data)
    print(quicksort(data))

if __name__ == "__main__":
    main()
