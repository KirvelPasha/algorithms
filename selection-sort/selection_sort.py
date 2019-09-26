def selection(data):
    for i in range(len(data) - 1):
        min = i
        for j in range(i + 1, len(data)):
            if data[j] < data[min]:
                min = j
        data[i], data[min] = data[min], data[i]

    return data


def main():
    data = [3, 8, 5, 4, 1, 9, -2]
    print(selection(data))


if __name__ == "__main__":
    main()
