def pageCount(n, p):
    if (p%2 != 0):
        p=p-1
    num_min = p//2
    num_min2 = (n-p)//2
    return min(num_min, num_min2)

if __name__=="__main__":
    print(pageCount(5,3))