def catAndMouse(x, y, z):
    if abs(x-z) < abs(y-z):
        return "Cat A"
    elif abs(x-z) > abs(y-z):
        return "Cat B"
    else:
        return "Mouse C"

if __name__ == "__main__":
   data = [[1,2,3],[1,3,2]]
   for i in data:
       print(catAndMouse(i[0],i[1],i[2]))

