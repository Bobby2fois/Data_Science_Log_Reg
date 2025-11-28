import sys
import math
import matplotlib.pyplot as plt

def read_csv(filepath):
    
    students = []
    with open(filepath, 'r') as f:
        headers = f.readline().strip().split(',')

        selected_features = [
            'Astronomy',
            'Herbology',
            'Ancient Runes',
            'Transfiguration',
            'Charms',
            'Flying'
        ]

        for line in f:
            values = line.strip().split(',')

            student = {
                'Index' : values[0],
                'House' : values[1],
            }
            
            if values[7]:
                student['Astronomy'] = float(values[7])
            else:
                student['Astronomy'] = None
            
            if values[8]:
                student['Herbology'] = float(values[8])
            else:
                student['Herbology'] = None

            if values[12]:
                student['Ancient Runes'] = float(values[12])
            else:
                student['Ancient Runes'] = None
            
            if values[14]:
                student['Transfiguration'] = float(values[14])
            else:
                student['Transfiguration'] = None
            
            if values[17]:
                student['Charms'] = float(values[17])
            else:
                student['Charms'] = None
            
            if values[18]:
                student['Flying'] = float(values[18])
            else:
                student['Flying'] = None

            students.append(student)

    return students, selected_features


def remove_incomplete_stud(students, features):

    complete_stud = []
    for student in students:
        is_complete = True
        for feature in features:
            if student[feature] is None:
                is_complete = False
                break
        if is_complete:
            complete_stud.append(student)

    return complete_stud


def create_matrix(students, features):

    X = []
    for student in students:
        row = []
        for feature in features:
            row.append(student[feature])
        X.append(row)
    
    return X


def create_house_vector(students):

    Y = []
    for student in students:
        Y.append(student['House'])
    return Y


def normalize_values(X):

    mean = [0] * 6
    std = [0] * 6
    variance = [0] * 6

    for i in range (len(X[0])):
        for row in X:
            mean[i] += (row[i])
    
    for j in range (len(mean)):
       mean[j] /= len(X)
    
    for k in range (len(X[0])):
        for row in X:
            variance[k] += (row[k] - mean[k])**2
    
    for h in range (len(variance)):
        variance[h] /= len(X)
        std[h] = math.sqrt(variance[h])
    
    i = 0
    j = 0

    for i in range(len(X)):
        for j in range(len(X[i])):
            X[i][j] = (X[i][j] - mean[j]) / std[j]

    return X, mean, std


def add_bias(X):

    X_with_bias = []

    for i in range(len(X)):
        row = []
        row.append(1.0)
        for j in range(len(X[i])):
            row.append(X[i][j])
        X_with_bias.append(row)

    return X_with_bias


def create_binary_label(Y, house):
    
    Y_binary = []
    for student in Y:
        if student == house:
            Y_binary.append(1)
        else:
            Y_binary.append(0)

    return Y_binary


def sigmoid(z):
    if z < -500:
        return 0.0
    elif z > 500:
        return 1.0
    else:
        return 1.0 / (1.0 + math.exp(-z))


def matrix_multiply(X, Y):
    ret = []
    i = 0

    for row in X:
        res = 0
        for i in range(len(row)):
            res += row[i] * Y[i]
        ret.append(res)
    return ret

def hypothesis(X, theta):
    z = matrix_multiply(X, theta)
    for i in range(len(z)):
        z[i] = sigmoid(z[i])
    return z

def compute_cost(X, Y, theta):

    m = len(X)
    h = hypothesis(X, theta)

    cost = 0
    for i in range(m):
        if Y[i] == 1:
            cost += math.log(h[i] + sys.float_info.epsilon)
        else:
            cost += math.log(1 - h[i] + sys.float_info.epsilon)
    cost = -cost / m

    return cost

def transpose(X):
    rows = len(X)
    cols = len(X[0])
    i = 0
    j = 0

    result = []
    for j in range(cols):
        new_row = []
        for i in range(rows):
            new_row.append(X[i][j])
        result.append(new_row)

    return result


def compute_gradient(X, Y, theta):
    
    m = len(X)
    h = hypothesis(X, theta)
    errors = []
    for i in range(len(h)):
        errors.append(h[i] - Y[i])

    X_T = transpose(X)
    gradient = []

    for row in X_T:
        grad_j = 0
        for i in range(len(row)):
            grad_j += row[i] * errors[i]
        gradient.append(grad_j / m)

    return gradient

def gradient_descent(X, Y, alpha, num_iterations):

    n_features = len(X[0])
    theta = [0.0] * n_features
    cost_history = []

    for iteration in range(num_iterations):
        gradient = compute_gradient(X, Y, theta)
        new_theta = []

        for j in range(len(theta)):
            new_theta.append(theta[j] - alpha * gradient[j])
        theta = new_theta

        cost = compute_cost(X, Y, theta)
        cost_history.append(cost)

    return theta, cost_history


def main():

    houses = ['Gryffindor', 'Hufflepuff', 'Slytherin', 'Ravenclaw']
    students, features = read_csv(sys.argv[1])
    students = remove_incomplete_stud(students, features)
    X = create_matrix(students, features)
    Y = create_house_vector(students)
    X_normalized, mean, std = normalize_values(X)
    X_with_bias = add_bias(X_normalized)
    all_theta = []
    alpha = 0.1
    num_iterations = 1000

    for i, house in enumerate(houses):
        Y_binary = create_binary_label(Y, house)
        theta, cost_history = gradient_descent(X_with_bias, Y_binary, alpha, num_iterations)
        all_theta.append(theta)
        fig, ax = plt.subplots()
        ax.plot(cost_history)
        plt.show()


if __name__ == "__main__":
    main()