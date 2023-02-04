import textwrap

def wrap(string, max_width):
    data = textwrap.wrap(string, max_width)
    cadena=''
    for i in data:
        cadena = cadena + i + "\n"
    return cadena


if __name__ == "__main__":
    string_d = "ABCDEFGHIJKLIMNOQRSTUVWXYZ"
    max_width = 4
    print(wrap(string_d, max_width))