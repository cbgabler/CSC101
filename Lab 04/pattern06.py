import driver

def letter(row, col):
    return 'X' if (row == col or row + col == 6) else 'O'

if __name__ == '__main__':
    driver.comparePatterns(letter)