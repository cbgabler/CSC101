import sys

if len(sys.argv) < 2:
    print('NO FILE NAME')
    exit()
data = 0
try:
    data_in = sys.argv[1]
    data = open(data_in, 'r')
except IndexError as ie:
    print('IndexError')
    exit()
except FileNotFoundError as fnf:
    print('File name not correct')
    exit()

for line in data:
    try:
        num_list = line.split()
        add = float(num_list[0]) + float(num_list[1])
        print(add)
    except IndexError:
        print('Error in text file.line missing or missing value')
    except ValueError:
        print('String in file')
