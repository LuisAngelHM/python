
def BirthdayCandles(arr):
    maximo = 0
    maxnum = 0
    for i in arr:
        if i > maximo:
            maximo = i
            maxnum = 0
        if maximo == i:
            maxnum += 1
    
    return maxnum

if __name__ == "__main__":
    array = [4,4,1,3]
    print(BirthdayCandles(array))