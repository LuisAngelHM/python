def reverseArray(a):
    reversed_array = []
    for i in range(len(a)-1,-1, -1):
        reversed_array.append(a[i])

    return reversed_array


if __name__ == "__main__":
    a = [1,2,3]
    print(reverseArray(a))