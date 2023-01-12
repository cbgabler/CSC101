import driver

def letter(row, col):
    return 'O' if (col >= 10) else 'X'

if __name__ == '__main__':
    driver.comparePatterns(letter)