import sys
import matplotlib.pyplot as plt

def read_csv(file_path):

    features = {}

    with open(file_path, 'r') as f:
        header_line = f.readline().strip()
        headers = header_line.split(',')
        for header in headers[6:]:
            features[header] = []

        for line in f:
            values = line.strip().split(',')
            for i, value in enumerate(values[6:], 6):
                if i < len(headers) and value:
                    features[headers[i]].append(float(value))
    return features

def main():

    if len(sys.argv) != 2:
        print("Usage: scatter_plot.py [filename]")
        sys.exit(1)
    
    dataset_file = sys.argv[1]
    features = read_csv(dataset_file)

    plt.scatter(features["Muggle Studies"], features["Ancient Runes"])
    plt.show()


if __name__ == "__main__":
    main()