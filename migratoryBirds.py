from statistics import multimode

def migratoryBirds(arr):
    mode = multimode(arr)
    mode.sort()
    return mode[0]


if __name__ == "__main__":
    arr = [1 ,2 ,3 ,4 ,5 ,4 ,3 ,2 ,1 ,3 ,4]
    print(migratoryBirds(arr))