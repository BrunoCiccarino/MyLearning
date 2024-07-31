from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics

# Load Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# n_neighborsint, default=5, Default number of neighbors to be used by default for neighbor queries.
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X, y)

species = knn.predict([[5.1, 3.5, 1.4, 0.2],
 [4.9, 3, 1.4, 0.2]]) 

print(iris.target_names[species])
