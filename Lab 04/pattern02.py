import driver

def letter(row, col):
    return 'Q' if (row >= 10) else 'R'

if __name__ == '__main__':
    driver.comparePatterns(letter)