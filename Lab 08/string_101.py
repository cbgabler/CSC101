def str_rot_13(string):
    new_string = ''
    for x in range(0, len(string)):
        if 97 <= ord(string[x]) <= 109 or 65 <= ord(string[x]) <= 77:
            new_string += chr(ord(string[x]) + 13)
        elif 110 <= ord(string[x]) <= 122 or 78 <= ord(string[x]) <= 90:
            new_string += chr(ord(string[x]) - 13)
        else:
            new_string += string[x]
    return new_string

def str_translate_101(string, c1, c2):
    new_string = ''
    for x in range(0, len(string)):
        if string[x] == c1:
            new_string += c2
        else:
            new_string += string[x]
    return new_string
