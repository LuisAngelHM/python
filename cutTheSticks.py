def removeCeros(arr):
    return [i for i in arr if i!=0]

def cutTheSticks(arr):
    number_items = []
    while len(arr) >= 1:
        number_items.append(len(arr))
        min_lenght = min(arr)
        arr = map(lambda x: x-min_lenght, arr)
        arr = removeCeros(arr)
    return number_items




if __name__ =="__main__":
    arr = [1, 2, 3, 4, 3, 3, 2, 1]
    print(cutTheSticks(arr))