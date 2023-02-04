import math 

def extraLongFactorials(n):
  return math.prod(range(1,n+1))


if __name__ == "__main__":
  print(extraLongFactorials(25))
