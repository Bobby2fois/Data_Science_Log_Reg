# Logistic Regression Implementation Guide

## Overview
This document outlines the step-by-step process of implementing logistic regression for house classification at Hogwarts based on student grades in various magical subjects.

## Data Flow

### 1. Data Loading
```python
read_csv(dataset.csv) -> List[Student]
```
**Output:** A list of student records with their house and grades.

```
Students: [
    [0, House, Astronomy, Herbology, Ancient Runes, Transfiguration, Charms, Flying],
    [1, House, Astronomy, Herbology, Ancient Runes, Transfiguration, Charms, Flying],
    [2, House, Astronomy, Herbology, Ancient Runes, Transfiguration, Charms, Flying],
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

## Model Training (Per House)

### 6. Binary Label Creation
```python
create_binary_label(Y, house) -> Y_binary
```
**Output:** Binary vector where 1 indicates the target house and 0 otherwise.

```
Y_binary: [
    [1],  # Belongs to target house
    [0],  # Doesn't belong
    [1],  # Belongs to target house
    ...
]
```

### 7. Gradient Descent
```python
gradient_descent(X_with_bias, Y_binary, alpha, num_iterations) -> (theta, cost_history)
```
- `alpha`: Learning rate
- `num_iterations`: Number of training iterations

#### 7a. Gradient Computation
```python
compute_gradient(X, Y, theta) -> gradient_vector
```
- `theta`: Parameter vector (size = number of features + 1)

##### 7aa. Hypothesis Function
```python
hypothesis(X, theta) -> sigmoid(X · theta)
```

##### 7ab. Matrix Transposition
```python
transpose(X) -> X_T
```
**Example:**
```
X_T: [
    [1.0, 1.0, 1.0, 1.0, 1.0, ...],
    [-1.0179, -1.1410, -0.7841, ...],
    [0.8699, -1.3750, 1.2528, ...],
    ...
]
```

#### 7b. Parameter Update
- Update theta based on computed gradients

#### 7c. Cost Computation
```python
compute_cost(X, Y, theta) -> cost_value
```
- Tracks training progress via `cost_history`

### 8. Model Storage
```python
all_theta.append(theta)
```
**Output:** Collection of theta vectors (one per house) for future predictions.