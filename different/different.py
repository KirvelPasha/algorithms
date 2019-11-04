# A simple program
# to find three elements whose
# sum is equal to zero
def findTriplets(arr):
    length = len(arr)
    for i in range(length-2):
        for j in range(i+1, length-1):
            for z in range(j+1, length):
                if arr[i] + arr[j] + arr[z] == 0:
                    print(arr[i], arr[j], arr[z])

def findTripletsH(arr):
    found = False
    length = len(arr)
    for i in range(length-1):
        s = set()
        for j in range(i+1, length):
            x = -(arr[i] + arr[j])
            if x in s:
                print(x, arr[i], arr[j])
                found = True
            else:
                s.add(arr[j])
    if not found:
        print("No")

def subArraySum(arr, sum):
    length = len(arr)

def main():
    arr = [0, -1, 2, -3, 1]
    # findTriplets(arr)
    # findTripletsH(arr)



if __name__ == "__main__":
    main()
