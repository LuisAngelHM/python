def jumpingOnClouds(c, k):
    countinueJump = True
    position = 0
    energy = 100
    
    while countinueJump :
        position = (position + k) % len(c)
        energy -= 1
        if (c[position] == 1):
            energy -= 2
        if position == 0:
            return energy

if __name__ == "__main__":

  print(jumpingOnClouds([0, 0, 1, 0, 0, 1, 1, 0], 2))