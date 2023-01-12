import driver

def letter(row, col):
    return 'T' if (col <= row - 1) else 'W'

if __name__ == '__main__':
    driver.comparePatterns(letter)