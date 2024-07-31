# it [always] returns a different result because <- KNN is deterministic
# basically loads the Iris dataset, splits it into training and testing sets
# and then uses the K-Nearest Neighbors (KNN) algorithm to iterate over different values
# of k (from 1 to 25 ). During each iteration, the code trains the KNN model with the training data
# makes predictions with the test data, and calculates the accuracy of the predictions. 
# The accuracy results for each k value are stored and printed.
 

from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics

# Load Iris dataset
iris = load_iris()
x = iris.data
y = iris.target

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.25)

performance_value = {}

# Loop to vary the value of k and calculate accuracy
for k in range(1, 26):
    knn = KNeighborsClassifier(n_neighbors=k) # n_neighbours Number of neighbors to use by default for kneighbors queries.
    knn.fit(X_train, y_train)
    predictions = knn.predict(X_test)
    accuracy = metrics.accuracy_score(y_test, predictions)
    performance_value[k] = accuracy
    print(f"k={k}, accuracy={accuracy * 100:.2f}%")

