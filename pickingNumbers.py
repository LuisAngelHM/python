from itertools import count


def pickingNumbers(a):
    numbers =list(set(a))
    if(len(numbers)==1):
        return len(a);
    count_numbers = [[a.count(i),i] for i in numbers]
    consecutives = []
    for i in range(len(numbers)-1):
        if abs(numbers[i] - numbers[i+1]) == 1:
            consecutives.append([numbers[i],numbers[i+1]])
    max_lenght = 0
    for consecutive in consecutives:
        addition = count_numbers[numbers.index(consecutive[0])][0] + count_numbers[numbers.index(consecutive[1])][0]
        if addition > max_lenght:
            max_lenght = addition
    if max([i[0] for i in count_numbers]) > max_lenght:
        return max([i[0] for i in count_numbers])
    return max_lenght

if __name__ == "__main__":
    a = [4,6,5,3,3,1]
    print(pickingNumbers(a))
    a = [1,2,2,3,1,2]
    print(pickingNumbers(a))
    a = "66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66"
    a = a.split(" ")
    a = [int(i) for i in a]
    print(pickingNumbers(a))

    a = "4 97 5 97 97 4 97 4 97 97 97 97 4 4 5 5 97 5 97 99 4 97 5 97 97 97 5 5 97 4 5 97 97 5 97 4 97 5 4 4 97 5 5 5 4 97 97 4 97 5 4 4 97 97 97 5 5 97 4 97 97 5 4 97 97 4 97 97 97 5 4 4 97 4 4 97 5 97 97 97 97 4 97 5 97 5 4 97 4 5 97 97 5 97 5 97 5 97 97 97"
    a = a.split(" ")
    a = [int(i) for i in a]
    print(pickingNumbers(a))