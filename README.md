# Hogwarts House Prediction using Logistic Regression

## Overview
This project implements a logistic regression model to predict the Hogwarts house of students based on their grades in various magical subjects. The implementation includes data preprocessing, model training, and prediction pipelines with proper handling of missing values.

## Project Structure
```
.
├── datasets/
│   ├── dataset_train.csv    # Training data with house labels
│   └── dataset_test.csv     # Test data for predictions
├── logreg_train.py         # Script for training the model
├── logreg_predict.py       # Script for making predictions
├── logreg_utils.py         # Shared utility functions
├── trained_model.csv       # Saved model parameters
└── houses.csv              # Prediction outputs
```

## Data Flow

### 1. Data Loading
#### Training Data
```python
read_csv_training(dataset_train.csv) -> (List[Student], List[str])
```
- Loads training data with house labels
- Returns list of student records and feature names

#### Prediction Data
```python
read_csv_predict(dataset_test.csv) -> (List[Student], List[str])
```
- Loads test data for prediction
- Handles missing values using training data statistics
- Returns list of student records and feature names

### 2. Data Preprocessing
#### Handling Missing Values
```python
replace_missing_values(students, features, means) -> List[Student]
```
- Replaces missing grade values with the mean from training data
- Ensures consistent handling of missing values between training and prediction

#### Feature Matrix Creation
```python
create_matrix(students, features) -> Matrix X
```
**Output:** A matrix containing only the grade values for each student.

```
X: [
    [Astronomy, Herbology, Ancient Runes, Transfiguration, Charms, Flying],
    [Astronomy, Herbology, Ancient Runes, Transfiguration, Charms, Flying],
    ...
]
```

### 2. Feature Matrix Creation
```python
create_matrix(students, features) -> Matrix X
```
**Output:** A matrix containing only the grade values for each student.

```
X: [
    [Astronomy, Herbology, Ancient Runes, Transfiguration, Charms, Flying],
    [Astronomy, Herbology, Ancient Runes, Transfiguration, Charms, Flying],
    [Astronomy, Herbology, Ancient Runes, Transfiguration, Charms, Flying],
    ...
]
```

### 3. House Vector Creation
```python
create_house_vector(students) -> Vector Y
```
**Output:** A vector containing house assignments for each student.

```
Y: [
    [Ravenclaw],
    [Slytherin],
    [Ravenclaw],
    ...
]
```

### 4. Data Normalization
```python
normalize_values(X) -> (std_dev, mean, X_normalized)
```
- Calculates standard deviation and mean for each course
- Returns normalized matrix X (values typically between ~-2 and 2)

### 5. Adding Bias Term
```python
add_bias(X_normalized) -> X_with_bias
```
**Output:** Augmented matrix with a leading 1.0 for each row (for θ₀ calculation).

```
X: [
    [1.0, -1.0179, 0.8699, 0.3464, 0.2207, 1.1997, -0.5077],
    [1.0, -1.1410, -1.3750, -1.2065, 0.6560, -1.0116, -1.3961],
    [1.0, -0.7841, 1.2528, 1.0073, 1.3184, 1.8215, 0.0803],
    ...
]
```

## Model Training

### 3. Training Pipeline
```python
# In logreg_train.py
students, features = read_csv_training("dataset_train.csv")
students = remove_incomplete_stud(students, features)
X = create_matrix(students, features)
Y = create_house_vector(students)
X_normalized, mean, std = normalize_values(X)
X_with_bias = add_bias(X_normalized)

# Train one-vs-all classifiers for each house
houses = ["Gryffindor", "Hufflepuff", "Slytherin", "Ravenclaw"]
all_theta = []
for house in houses:
    Y_binary = create_binary_label(Y, house)
    theta, _ = gradient_descent(X_with_bias, Y_binary, alpha=0.1, num_iterations=1000)
    all_theta.append(theta)

# Save model parameters
save_model("trained_model.csv", houses, all_theta)
```

### 4. Model Parameters
- Learning rate (α): 0.1
- Number of iterations: 1000
- Regularization: None
- Features: Astronomy, Herbology, Ancient Runes, Transfiguration, Charms, Flying

## Prediction Pipeline

### 1. Loading the Model
```python
# In logreg_predict.py
thetas = load_thetas("trained_model.csv")
houses = list(thetas.keys())
```

### 2. Making Predictions
```python
def predict_house(X, thetas, houses):
    predictions = []
    for x in X:
        max_prob = -1
        predicted_house = None
        for house in houses:
            theta = thetas[house]
            z = sum(xi * ti for xi, ti in zip(x, theta))
            prob = sigmoid(z)
            if prob > max_prob:
                max_prob = prob
                predicted_house = house
        predictions.append(predicted_house)
    return predictions
```

### 3. Output Format
Predictions are saved in `houses.csv` with the following format:
```
Index,Hogwarts House
0,Gryffindor
1,Slytherin
2,Ravenclaw
...
```

## Running the Code

### Training the Model
```bash
python3 logreg_train.py datasets/dataset_train.csv
```

### Making Predictions
```bash
python3 logreg_predict.py datasets/dataset_test.csv trained_model.csv
```

## Error Handling
- Missing values in test data are replaced with the mean from training data
- Invalid or malformed input files raise appropriate exceptions
- Model parameters are validated before prediction