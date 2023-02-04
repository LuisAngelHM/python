


from audioop import reverse


if __name__ == "__main__":
    commands = []
    data = []
    for i in range(4):
        line = input()
        commands.append(line)
    for i in commands:
        command = i.split()
        if command[0] == "insert":
            data.insert(int(command[1]),int(command[2]))
        elif command[0] == "print":
            print(data)
        elif command[0] == "remove":
            data.remove(int(command[1]))
        elif command[0] == "append":
            data.append(int(command[1]))
        elif command[0] == "sort":
            data.sort()
        elif command[0] == "pop":
            data.pop()
        elif command[0] == "reverse":
            data = data[::-1]