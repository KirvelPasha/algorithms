import random
def bubbleSort(data):
    length = len(data)
    for i in range(length - 1):
        for j in range(length - i - 1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
    return data

def main():
    data = [random.randrange(-10, 10) for i in range(10)]
    print(bubbleSort(data))

if __name__ == "__main__":
        main()
