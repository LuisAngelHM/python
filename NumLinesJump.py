def NumLineJumps(x1,v1,x2,v2):
    b=True
    t = 1
    while b:
        if(x1+v1*t) == (x2+v2*t):
            print("YES")
            b=False
        if t>1000:
            print("NO")
            b=False
        t += 1

if __name__ == "__main__":
    NumLineJumps(14,4,98,2)