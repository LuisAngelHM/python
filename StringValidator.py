def StringValidator(string):
    for i in string:
        if i.isalnum():
            print("True")
            break    
        if string.isalpha():
            print("True")
            break
    if string.isalnum() is True and string.isalpha() is False:
        print("True")
    else:
        print("False")
    if string.isupper() is False:
        print("True")
    else:
        print("False")
    if string.islower() is False:
        print("True")
    else:
        print("False")

if __name__ == "__main__":
    string = "##2"
    StringValidator(string)