def appendAndDelete(s, t, k):
    prefix = 0
    for c1, c2 in zip(s, t):
        if c1 == c2:
            prefix += 1
        else:
            break
    if k >= len(s) + len(t):
        return "Yes"
    elif k >= len(s) + len(t) - 2 * prefix and k % 2 == (len(s) + len(t)) % 2:
        return "Yes"
    else:
        return "No"


if __name__ == '__main__':
    s = "hackerhappy"
    t = "hackerrank"
    print(appendAndDelete(s,t,9))
    s = "aba"
    t = "aba"
    print(appendAndDelete(s,t,7))
    s = "abcd"
    t = "abcdert"
    print(appendAndDelete(s,t,2))
