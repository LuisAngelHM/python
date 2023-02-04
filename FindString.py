def FindString(string, substring):
    num = 0
    find_sub = string.find(substring,0)
    while find_sub != -1:
        num += 1
        find_sub = string.find(substring, find_sub+1)
    return num

if __name__== "__main__":
    string = "ABCDCDC"
    substring = "CDC"
    print(FindString(string, substring)) 