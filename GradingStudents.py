from operator import mod


def gradingStudents(grades):
    nums = []
    for num in grades:
        if num >= 38:
            if num % 5 == 0:
                nums.append(num)
            else:
                multiple = num + (5-(num%5))
                print(multiple)
                if (multiple-num < 3):
                    nums.append(multiple)
                else:
                    nums.append(num)    
        else:
            nums.append(num)
    return(nums)        





if __name__ =="__main__":
    grades = [58,37,65,45,49,52,80,78]
    print(gradingStudents(grades))