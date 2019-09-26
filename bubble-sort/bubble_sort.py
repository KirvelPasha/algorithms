def bubbleSort(data):
    length = len(data)
    for i in range(length-1):
        for j in range(length - i - 1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
    return data

def main():
    data = [3, 8, 5, 4, 1, 9, -2]
    print(bubbleSort(data))

if __name__ == "__main__":
        main()
