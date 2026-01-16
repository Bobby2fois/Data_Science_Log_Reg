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

    def wrap_feature_name(name, max_length=15):
        """Wrap long feature names into multiple lines"""
        if len(name) <= max_length:
            return name
        words = name.split()
        lines = []
        current_line = []
        current_length = 0
        
        for word in words:
            if current_length + len(word) + 1 <= max_length:
                current_line.append(word)
                current_length += len(word) + 1
            else:
                if current_line:
                    lines.append(' '.join(current_line))
                current_line = [word]
                current_length = len(word)
        
        if current_line:
            lines.append(' '.join(current_line))
        
        return '\n'.join(lines)
    
    wrapped_names = [wrap_feature_name(name) for name in feature_names]

    fig, axes = plt.subplots(n, n, figsize=(15, 15))

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
                ax.set_ylabel(wrapped_names[i], fontsize=7)
            if i == n - 1:
                ax.set_xlabel(wrapped_names[j], fontsize=7, rotation=0, ha='right')
            
            ax.set_xticks([])
            ax.set_yticks([])
    
    if n > 1:
        handles, labels = axes[0, 1].get_legend_handles_labels()
        fig.legend(handles, labels, loc='upper left', fontsize=7, markerscale=3, 
                   frameon=True, fancybox=True, shadow=True)
    
    plt.subplots_adjust(left=0.08, right=0.95, top=0.95, bottom=0.06, hspace=0.15, wspace=0.15)
    plt.show()

if __name__ == "__main__":
    main()