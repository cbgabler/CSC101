def is_lower_101(char):
    if 97 <= ord(char) <= 127:
        return True
    else:
        return False


def char_rot_13(char):
    if 97 <= ord(char) <= 109 or 65 <= ord(char) <= 77:
        return chr(ord(char) + 13)
    elif 110 <= ord(char) <= 122 or 78 <= ord(char) <= 90:
        return chr(ord(char) - 13)
    else:
        return char
