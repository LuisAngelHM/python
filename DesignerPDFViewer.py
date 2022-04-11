def DesignerPDFViewer(word, h):
    return max([h[ord(i)-97] for i in word])*len(word)


if __name__ == "__main__":
    word = "zaba"
    h=[1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,7]
    print(DesignerPDFViewer(word, h))