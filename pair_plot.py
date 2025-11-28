import sys
import matplotlib.pyplot as plt
import math

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
                    else:
                        features[headers[i]]["Gryffindor"].append(float('nan'))
            elif values[1] == "Hufflepuff":
                for i, value in enumerate(values[6:], 6):
                    if value:
                        features[headers[i]]["Hufflepuff"].append(float(value))
                    else:
                        features[headers[i]]["Hufflepuff"].append(float('nan'))
            elif values[1] == "Ravenclaw":
                for i, value in enumerate(values[6:], 6):
                    if value:
                        features[headers[i]]["Ravenclaw"].append(float(value))
                    else:
                        features[headers[i]]["Ravenclaw"].append(float('nan'))
            elif values[1] == "Slytherin":
                for i, value in enumerate(values[6:], 6):
                    if value:   
                        features[headers[i]]["Slytherin"].append(float(value))
                    else:
                        features[headers[i]]["Slytherin"].append(float('nan'))
            

    return features

def main():

    if len(sys.argv) != 2:
        print("Usage: pair_plot.py [Filename]")
        sys.exit(1)
    
    filename = sys.argv[1]
    features = read_csv(filename)
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
    colors = {'Gryffindor': 'blue', 'Hufflepuff': 'yellow', 'Ravenclaw': 'green', 'Slytherin': 'red'}

    feature_names = list(features.keys())
    n = len(feature_names)

    fig, axes = plt.subplots(n, n, figsize=(13,13))

    for i, feature1 in enumerate(feature_names):
        for j, feature2 in enumerate(feature_names):
            if n > 1:
                ax = axes[i, j]
            else:
                ax = axes

            if i == j:
                for house in houses:
                    ax.hist(features[feature1][house], alpha=0.5, label=house, color=colors[house], bins=20)
            else:
                for house in houses:
                    x_values = features[feature1][house]
                    y_values = features[feature2][house]
                    ax.scatter(x_values, y_values, s=1, c=colors[house], label=house if i==0 and j==1 else "", alpha=1)

            if j == 0:
                ax.set_ylabel(feature1, fontsize=7)
            if i == n - 1:
                ax.set_xlabel(feature2, fontsize=7)
            
            ax.set_xticks([])
            ax.set_yticks([])
    
    if n > 1:
        handles, labels = axes[0, 1].get_legend_handles_labels()
        fig.legend(handles, labels, loc='lower right')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()