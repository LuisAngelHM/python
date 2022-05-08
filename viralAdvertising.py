from multiprocessing import shared_memory


def viralAdvertising(n):
    data = [[5,2,2]]
    for i in range(1,n):
        shared = (data[i-1][0]//2) * 3 
        liked = shared // 2
        comulative = data[i-1][2]+liked
        data.append([shared, liked, comulative])
    return data[n-1][2]

if __name__ == "__main__":

    print(viralAdvertising(1000))