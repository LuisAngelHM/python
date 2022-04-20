def sockMerchant(n, ar):
    nums = 0
    array_unique = list(set(ar))
    for i in array_unique:
        nums += ar.count(i)//2
    return nums
if __name__ == "__main__":
    data = [1,2,1,2,3,2,1]
    print(sockMerchant(len(data),data))