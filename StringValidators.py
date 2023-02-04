def StringValidator(string_data):
    is_array = [False, False, False, False, False]

    for s in string_data:
        if s.isalnum() and is_array[0] is False:
            is_array[0] = True
        if s.isalpha() and  is_array[1] is False:
            is_array[1] = True
        if s.isdigit() and is_array[2] is False:
            is_array[2] = True
        if s.islower() and is_array[3] is False:
            is_array[3] = True
        if s.isupper() and is_array[4] is False:
            is_array[4] = True
    for i in is_array:
        print(i)

if __name__ == "__main__":
    string_data = "qA2"
    StringValidator(string_data)
