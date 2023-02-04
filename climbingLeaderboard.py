import time


def climbingLeaderboard(ranked, player):
    ranked_player = []
    ranked_original = ranked
    ranked = []
    for i in ranked_original:
        if i not in ranked:
            ranked.append(i)
    for i in player:
        if i not in ranked:
            if i > ranked[0]:
                ranked.insert(0,i)
                ranked_player.append(1)
            elif i < ranked[-1]:
                ranked.append(i)
                ranked_player.append(len(ranked))
            else:
                isIn = False
                j = 0
                while j < len(ranked)-1 and isIn == False:
                    if i < ranked[j] and i > ranked[j+1]:
                        ranked.insert(j+1,i)
                        ranked_player.append(j+2)
                        isIn = True
                    j += 1
        else:
            ranked_player.append(ranked.index(i)+1)
    return ranked_player





if __name__ == "__main__":
    ranked = [100 ,100, 50, 40, 40, 20, 10]
    player = [5, 25, 50, 120]
    print(climbingLeaderboard(ranked, player))

    