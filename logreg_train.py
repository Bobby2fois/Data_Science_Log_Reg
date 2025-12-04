import sys
import logreg_utils

def main():

    houses = ['Gryffindor', 'Hufflepuff', 'Slytherin', 'Ravenclaw']
    students, features = logreg_utils.read_csv_training(sys.argv[1])
    students = logreg_utils.remove_incomplete_stud(students, features)

    X = logreg_utils.create_matrix(students, features)
    Y = logreg_utils.create_house_vector(students)
    X_normalized, mean, std = logreg_utils.normalize_values(X)
    X_with_bias = logreg_utils.add_bias(X_normalized)
    all_theta = []
    alpha = 0.1
    num_iterations = 1000

    for i, house in enumerate(houses):
        Y_binary = logreg_utils.create_binary_label(Y, house)
        theta, cost_history = logreg_utils.gradient_descent(X_with_bias, Y_binary, alpha, num_iterations)
        all_theta.append(theta)

    with open("datasets/weights.csv", "w") as f:
        for i, house in enumerate(houses):
            theta_str = ','.join(map(str, all_theta[i]))
            f.write(f"{house},{theta_str}\n")



if __name__ == "__main__":
    main()