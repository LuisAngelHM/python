import string
def missingCharacters(s):
    data = [str(x) for x in range(0,10)]
    data = data + list(string.ascii_lowercase)
    for c in s:
        try:
            data.remove(c)
        except:
            pass
    return''.join(data)

if __name__ =="__main__":
    s = "8hypotheticall024y6wxz"
    print(missingCharacters(s))