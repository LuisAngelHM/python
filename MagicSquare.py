import sys
def getCost(square, magic):
    cost = 0
    for i in range(3):
        for j in range(3):
            cost += abs(square[i][j] - magic[i][j])
    return cost
def formingMagicSquare(s):
    all_magics=[
        [[8,1,6],[3,5,7],[4,9,2]],
        [[6,1,8],[7,5,3],[2,9,4]],
        [[4,9,2],[3,5,7],[8,1,6]],
        [[2,9,4],[7,5,3],[6,1,8]],
        [[8,3,4],[1,5,9],[6,7,2]],
        [[4,3,8],[9,5,1],[2,7,6]],
        [[6,7,2],[1,5,9],[8,3,4]],
        [[2,7,6],[9,5,1],[4,3,8]]
    ]
    cost = sys.maxsize
    cost_temp = 0
    for square in all_magics:
        cost_temp = getCost(square, s)
        cost = min(cost, cost_temp)
    return cost

if __name__ == "__main__":
    magic =[[4, 4, 7],[3, 1, 5],[1, 7, 9]]
    print(formingMagicSquare(magic))