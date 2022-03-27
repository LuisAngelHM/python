def SubArrayDivision(_array,m,d):
    waysPossible = 0
    for i in range(len(_array)):
        print(_array[i:i+m])
        if sum(_array[i:i+m])==d:
            waysPossible += 1
    return waysPossible

if __name__ == "__main__":
    array_ = [1,]
    d = 3
    m = 2
    SubArrayDivision(array_, m, d)
  