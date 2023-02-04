def beautifulDays(i, j, k):
    return(len([x for x in range(i,j+1) if (x - int(str(x)[::-1])) % k == 0]))
if __name__ == "__main__":
    i=20
    j=23
    k=6
    print(beautifulDays(i,j,k))
