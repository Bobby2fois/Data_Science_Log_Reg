import sys
import matplotlib.pyplot as plt
import math

def read_csv(filename):

    data = {}
    houses = []

    with open(filename, 'r') as f:
        headers = f.readline().strip().split(',')
        for header in headers[6:]:
            data[header] = []
        for line in f:
            values = line.strip().split(',')
            for i, value in enumerate(values[6:], 6):
                if value:
                    data[headers[i]].append(float(value))
                else:
                    data[headers[i]].append(float('nan'))
            houses.append(values[1])
    return data, houses

def main():

    if len(sys.argv != 2):
        print("Usage: pair_plot.py [Filename]")
        sys.exit(1)
    
    filename = sys.argv[1]


if __name__ == "__main__":
    main()