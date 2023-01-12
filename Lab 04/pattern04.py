import driver

def letter(row, col):
    return 'M' if (3 <= col <= 6 and 2 <= row <= 4) else 'S'

if __name__ == '__main__':
    driver.comparePatterns(letter)