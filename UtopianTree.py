heights = [1]


def getHeights(x):
    global heights
    for j in range(len(heights), x+1):
        if j%2==0:
            heights.append(heights[-1]+1)
        else:
            heights.append(heights[-1]*2)
    
def utopianTree(n): 
    getHeights(n)
    return heights[n]




if __name__ == "__main__":
    
    periods = [0,1,4,7]
    for i in periods:
        print(utopianTree(i))