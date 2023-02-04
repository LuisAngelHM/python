def breakingRecords(scores):
    result = [0,0]
    max_n = scores[0]
    min_n = scores[0]
    for i in scores:
        if i > max_n:
            max_n = i
            result[0]+=1
        elif i < min_n:
            min_n = i
            result[1]+=1
    return result

if __name__ == "__main__":
    print(breakingRecords([3,4, 21, 36, 10, 28, 35, 5, 24, 42]))