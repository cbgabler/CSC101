import driver

def letter(row, col):
    if (2 <= row <= 3) and (4 <= col <= 9) or (4 <= row <= 5 and 4 <= col <= 6):
        return 'Z'
    elif (4 <= row <= 5 and 10 <= col <= 12) or (row == 6 and 7 <= col <= 12):
        return 'B'
    elif (4 <= row <= 5 and 7 <= col <= 9):
        return 'X'
    else:
        return 'T'

if __name__ == '__main__':
    driver.comparePatterns(letter)