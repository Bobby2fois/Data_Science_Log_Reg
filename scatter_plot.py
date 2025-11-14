import sys
import matplotlib.pyplot as plt


def main():
    # Create properly aligned pairs
    astronomy_values = []
    defense_values = []
    houses = []


    if len(sys.argv) != 2:
        print("Usage: scatter_plot.py [filename]")
        sys.exit(1)
    dataset_file = sys.argv[1]

    with open(dataset_file, 'r') as f:
        headers = f.readline().strip().split(',')
        astro_idx = headers.index('Astronomy')
        defense_idx = headers.index('Defense Against the Dark Arts')
        house_idx = headers.index('Hogwarts House')
        
        for line in f:
            values = line.strip().split(',')
            if len(values) > max(astro_idx, defense_idx) and values[astro_idx] and values[defense_idx]:
                try:
                    astronomy_values.append(float(values[astro_idx]))
                    defense_values.append(float(values[defense_idx]))
                    houses.append(values[house_idx])
                except ValueError:
                    pass

    # Now plot only properly paired values
    colors = {'Gryffindor': 'red', 'Hufflepuff': 'yellow', 'Ravenclaw': 'blue', 'Slytherin': 'green'}
    for house in set(houses):
        x = [astronomy_values[i] for i in range(len(houses)) if houses[i] == house]
        y = [defense_values[i] for i in range(len(houses)) if houses[i] == house]
        plt.scatter(x, y, c=colors.get(house, 'black'), label=house, alpha=0.7)

    plt.xlabel("Astronomy")
    plt.ylabel("Defense Against the Dark Arts")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()