import random


# A simple program
# to find three elements whose
# sum is equal to zero
def findTriplets(arr):
    length = len(arr)
    for i in range(length - 2):
        for j in range(i + 1, length - 1):
            for z in range(j + 1, length):
                if arr[i] + arr[j] + arr[z] == 0:
                    print(arr[i], arr[j], arr[z])


def findTripletsH(arr):
    found = False
    length = len(arr)
    for i in range(length - 1):
        s = set()
        for j in range(i + 1, length):
            x = -(arr[i] + arr[j])
            if x in s:
                print(x, arr[i], arr[j])
                found = True
            else:
                s.add(arr[j])
    if not found:
        print("No")


# Estimate pi, given that you have random (0, 1)
def estimate_pi(n):
    num_point_circle = 0
    num_point_total = 0
    for i in range(n):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        distance = x ** 2 + y ** 2
        if distance <= 1:
            num_point_circle += 1
        num_point_total += 1

    return 4 * num_point_circle / num_point_total


def main():
    # arr = [0, -1, 2, -3, 1]
    # findTriplets(arr)
    # findTripletsH(arr)
    print(estimate_pi(1000000))


if __name__ == "__main__":
    main()
