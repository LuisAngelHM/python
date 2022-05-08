def circularArrayRotation(a, k, queries):
    for i in range(k):
        a.insert(0,a.pop())
    result = []
    for i in queries:
        result.append(a[i])
    return result

if __name__=="__main__":
    a =[3,4,5]
    k = 2
    queries = [1,2]
    circularArrayRotation(a,k,queries)
