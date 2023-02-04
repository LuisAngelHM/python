def angryProfessor(k, a):
    students = [i for i in a if i<=0]
    if len(students) >= k:
        return "NO"
    return "YES"

if __name__ == "__main__":
    k = 2
    a = [0, -1, 2, 1]
    print(angryProfessor(k,a))