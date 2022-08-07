def hourglassSum(arr):
    matrixs = []
    matrix_final = []
    major = -10000 
    for i in range(0,6):
        matrix = []
        for j in range(0,4):
            matrix.append(arr[i][j:j+3])
        matrixs.append(matrix)
    for l in range(0,4):
        for k in range(0,4):
            matrix_temp = []
            for i in range(0+k,3+k):
                matrix_temp.append(matrixs[i][l])
            matrix_final.append(matrix_temp)
    for i in matrix_final:
        sum_temp = 0
        for j,p in enumerate(i):
            if j==1:
                sum_temp = sum_temp + sum(p) -p[0] - p[2]
            else:
                sum_temp = sum_temp + sum(p)
        if sum_temp > major:
            major = sum_temp
    return major

if __name__ == "__main__":
    arr=[   [-9, -9, -9 , 1, 1, 1], 
            [0, -9,  0,  4, 3, 2],
            [-9, -9, -9,  1, 2, 3],
            [0,  0,  8,  6, 6, 0],
            [0,  0,  0, -2, 0, 0],
            [0,  0,  1,  2, 4, 0]
        ]
    print(hourglassSum(arr))

    arra = [[1, 1, 1, 0, 0, 0],
            [0, 1, 0, 0, 0, 0],
            [1, 1, 1, 0, 0, 0],
            [0, 0, 2, 4, 4, 0],
            [0, 0, 0, 2, 0, 0],
            [0, 0, 1, 2, 4, 0]]

    print(hourglassSum(arra))