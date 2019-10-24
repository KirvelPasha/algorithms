def insertion(data):
    for i in range(len(data)):
        j = i - 1
        key = data[i]
        while data[j] > key and j >= 0:
            data[j + 1] = data[j]
            j -= 1
        data[j+1] = key
    return data

def main():
    data = [3, 8, 5, 4, 1, 9, -2]
    print(insertion(data))

if __name__ == "__main__":
        main()
