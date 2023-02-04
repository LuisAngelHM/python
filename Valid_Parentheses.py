def valid_parentheses(s):
    cola = []
    for i in s:
        if i == '(' or i == '{' or i == '[':
            cola.append(i)
        else:
            
            t = cola[-1]
            if ( i== '}' and t == '{' ) or ( i==')' and t =='(' ) or (i==']' and t == '['):
                cola.pop()
    if not cola:
        return 'valid'
    else:
        return 'invalid'




if __name__ == "__main__":
    string = "{}"
    print(valid_parentheses(string))