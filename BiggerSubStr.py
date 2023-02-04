def biggerSubstring(s):
    max_sbstr = 0
    for i in range(len(s)):
        repeat = False
        sbstr = list()
        sbstr.append(s[i])
        j = i+1
        while(j < len(s) and repeat == False):
            if s[j] not in sbstr:
                sbstr.append(s[j])
            else:
                max_sbstr = max(len(sbstr),max_sbstr)  
                repeat = True
            j = j + 1
    return max_sbstr



if __name__ == "__main__":
    s="enjoyalgorithms"
    print(biggerSubstring(s))