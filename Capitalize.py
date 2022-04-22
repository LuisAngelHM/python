def solve(s):
    data = s.split(' ')
    data = map(lambda x: x.capitalize(), data)
    return " ".join(data)

if __name__ == "__main__":
    print(solve("hola mundo como estas"))