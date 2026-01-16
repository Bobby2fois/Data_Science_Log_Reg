import sys
import logreg_utils

def main():

    train_students, train_features = logreg_utils.read_csv_training("datasets/dataset_train.csv")
    train_students = logreg_utils.remove_incomplete_stud(train_students, train_features)
    train_X = logreg_utils.create_matrix(train_students, train_features)
    train_X_normalized, means, std = logreg_utils.normalize_values(train_X)


    houses = ["Gryffindor", "Hufflepuff", "Slytherin", "Ravenclaw"]
    students, features = logreg_utils.read_csv_predict(sys.argv[1])
    students = logreg_utils.replace_missing_values(students, features, means)
    X = logreg_utils.create_matrix(students, features)
    X, _, _ = logreg_utils.normalize_values(X)
    X = logreg_utils.add_bias(X)
    thetas = logreg_utils.load_thetas(sys.argv[2])
    predictions = logreg_utils.predict_house(X, thetas, houses)
    with open('houses.csv', 'w') as f:
        f.write("Index,Hogwarts House\n")
        for i, student in enumerate(students):
            f.write(f"{student['Index']},{predictions[i]}\n")

if __name__ == "__main__":
    main()