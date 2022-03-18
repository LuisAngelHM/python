def mutate_string(string, position, character):
    string = list(string)
    string.insert(position, character)
    string = ''.join(string)
    return string

if __name__ == "__main__":
    s = "aabbbssgd"
    mutate_string(s, 3, 'p')