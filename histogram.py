import sys
import matplotlib.pyplot as plt

def read_csv(file_path):
    features = {}
    
    with open(file_path, 'r') as f:
        header_line = f.readline().strip()
        headers = header_line.split(',')
        for header in headers[6:]:
            features[header] = {}
        
        for header in features:
            features[header]["Gryffindor"] = []
            features[header]["Hufflepuff"] = []
            features[header]["Ravenclaw"] = []
            features[header]["Slytherin"] = []

        for line in f:
            values = line.strip().split(',')
            if values[1] == "Gryffindor":
                for i, value in enumerate(values[6:], 6):
                    if value:
                        features[headers[i]]["Gryffindor"].append(float(value))
            elif values[1] == "Hufflepuff":
                for i, value in enumerate(values[6:], 6):
                    if value:
                        features[headers[i]]["Hufflepuff"].append(float(value))
            elif values[1] == "Ravenclaw":
                for i, value in enumerate(values[6:], 6):
                    if value:
                        features[headers[i]]["Ravenclaw"].append(float(value))
            elif values[1] == "Slytherin":
                for i, value in enumerate(values[6:], 6):
                    if value:
                        features[headers[i]]["Slytherin"].append(float(value))
            

    return features

def main():
    if len(sys.argv) != 2:
        print("Usage: histogram.py [filename]")
        sys.exit(1)
    dataset_file = sys.argv[1]
    x = read_csv(dataset_file)

    for header in x:
        plt.hist(x[header]["Gryffindor"], alpha=0.5, label="Gryffindor", color="red", bins=20)
        plt.hist(x[header]["Hufflepuff"], alpha=0.5, label="Hufflepuff", color="yellow", bins=20)
        plt.hist(x[header]["Ravenclaw"], alpha=0.5, label="Ravenclaw", color="blue", bins=20)
        plt.hist(x[header]["Slytherin"], alpha=0.5, label="Slytherin", color="green", bins=20)
        plt.title(header)
        plt.xlabel("Score")
        plt.ylabel("Frequency")
        plt.legend()
        plt.show()


if __name__ == "__main__":
    main()