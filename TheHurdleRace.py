def TheHurdleRace(height,k):
    return  0 if max(height) - k < 0 else max(height) - k
    


if __name__ == "__main__":
    height = [1,6,3,5,2]
    k = 4
    print(TheHurdleRace(height,k))