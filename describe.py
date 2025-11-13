import sys
import math

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

def find_min(values):
    min_val = values[0]
    for val in values[1:]:
        if val < min_val:
            min_val = val
    return min_val

def find_max(values):
    max_val = values[0]
    for val in values[1:]:
        if val > max_val:
            max_val = val
    return max_val

def count_Mean(values):
    count = 0
    total_sum = 0
    for value in values:
        count += 1
        total_sum += value
    mean = total_sum/count
    return count, mean

def std(values, mean, count):
    sum_squared_diff = 0
    for val in values:
        sum_squared_diff += (val - mean) ** 2
    variance = sum_squared_diff / count
    std = math.sqrt(variance)
    return std

def first_quartile(values, count):
    sorted_values = sorted(values)
    return sorted_values[int(count * 0.25)]

def third_quartile(values, count):
    sorted_values = sorted(values)
    return sorted_values[int(count * 0.75)]

def median(values, count):
    sorted_values = sorted(values)
    return sorted_values[int(count / 2)]


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 describe.py [filename]")
        sys.exit(1)
    
    dataset_file = sys.argv[1]
    stats = {}
    try:
        features = read_csv(dataset_file)

        for header in features:
            print(f"{header}:\n")
            stats[header] = {}
            try:
                stats[header]['min'] = find_min(features[header])
                print(f"min = {stats[header]['min']}")
            except Exception as e:
                print(f"error find_min for {header}: {e}")
            try:
                stats[header]['max'] = find_max(features[header])
                print(f"max = {stats[header]['max']}")
            except Exception as e:
                print(f"error find_max for {header}: {e}")
            try:
                stats[header]['count'] = count_Mean(features[header])[0]
                print(f"count = {stats[header]['count']}")
            except Exception as e:
                print(f"error count_Mean(count) for {header}: {e}")
            try:
                stats[header]['mean'] = count_Mean(features[header])[1]
                print(f"mean = {stats[header]['mean']}")
            except Exception as e:
                print(f"error count_mean(mean) for {header}: {e}")
            try:
                stats[header]['std'] = std(features[header], stats[header]['mean'], stats[header]['count'])
                print(f"std = {stats[header]['std']}")
            except Exception as e:
                print(f"error std(std) for {header}: {e}")
            try:
                stats[header]['25'] = first_quartile(features[header], stats[header]['count'])
                print(f"25% = {stats[header]['25']}")
            except Exception as e:
                print(f"error 25% for {header}: {e}")
            try:
                stats[header]['50'] = median(features[header], stats[header]['count'])
                print(f"50% = {stats[header]['50']}")
            except Exception as e:
                print(f"error 50% for {header}: {e}")
            try:
                stats[header]['75'] = third_quartile(features[header], stats[header]['count'])
                print(f"75% = {stats[header]['75']}\n\n")
            except Exception as e:
                print(f"error 75% for {header}: {e}")
        
        # for header in features:
        #     print(f"{header}".ljust(15), end="")
        # print()  # This adds the newline after all headers are printed

        # # Print statistics
        # for stat in ['count', 'mean', 'std', 'min', '25', '50', '75', 'max']:
        #     print(f"{stat}".ljust(8), end="")
        #     for header in features:
        #         print(f"{stats[header][stat]:.6f}".ljust(15), end="")
        #     print()
    
    except FileNotFoundError:
        print("File not found")
        sys.exit(1)
        
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()