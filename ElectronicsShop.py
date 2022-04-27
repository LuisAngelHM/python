def getMoneySpent(keyboards, drives, b):
    max_spent = -1   
    for keyboard in keyboards:
        for drive in drives:
            addition = keyboard + drive
            if addition <= b:
                if addition > max_spent:
                   max_spent = addition 
    return max_spent
    
if __name__ =="__main__":
    b=5
    keyboards = [4]
    USBdrive = [5]
    print(getMoneySpent(keyboards,USBdrive,b))

    