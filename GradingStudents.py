from operator import mod


def gradingStudents(grades):
    nums = []
    for num in grades:
        if num % 5 == 0 or (5-(num%5))>2 or num<38:
                nums.append(num)
        else:
            multiple = num + (5-(num%5))
            nums.append(multiple) 
    return(nums)        





if __name__ =="__main__":
    grades = [58,37,65,45,49,52,80,78,37,48,69]
    print(gradingStudents(grades))