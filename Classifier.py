import numpy as np
from sklearn import neighbors, svm, neural_network, model_selection, metrics

class Classifier:
  def __init__(self):
    A = np.loadtxt('./datasets-part1/tictac_final.txt')
    X = A[:,:9]
    y = list(np.concatenate(A[:, 9:]).flat) # Formats y into a single vector

    print("K-NEAREST NEIGHBORS")
    print("===================================")
    self.k_nearest(X, y)
    print("")
    print("LINEAR SVM")
    print("===================================")
    self.linear_svc(X, y)
    print("")
    print("MULTILAYER PERCEPTRON")
    print("===================================")
    self.perceptron(X, y)
  
  def confusion_matrix(self, matrix):
    head_template = "{0:10}{1:13}{2:13}"
    body_template = "{0:10}{1:12,.6f}{2:13,.6f}"
    print(head_template.format("", "PREDICTED -1", "PREDICTED +1"))
    print("")
    print(body_template.format("ACTUAL -1", matrix[0][0], matrix[0][1]))
    print("")
    print(body_template.format("ACTUAL +1", matrix[1][0], matrix[1][1]))
  
  def k_nearest(self, X, y):
    # Split data into training and testing sets 80/20 at random
    # Shuffle dataset before splitting
    X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.2, random_state=42, shuffle=True)

    # Build and train classifier on training data
    classifier = neighbors.KNeighborsClassifier(n_neighbors=10)
    classifier.fit(X_train, y_train)

    # Use the model to generate a prediction using the testing data
    y_pred = classifier.predict(X_test)

    # Generate a confusion matrix to display model accuracy on testing data
    # matrix = metrics.confusion_matrix(y_test, y_pred)
    matrix = [ row / np.linalg.norm(row) for row in metrics.confusion_matrix(y_test, y_pred) ]
    self.confusion_matrix(matrix)
    print("")
    print("Model Accuracy: %0.6f" % metrics.accuracy_score(y_test, y_pred))

  def linear_svc(self, X, y):
    # Split data into training and testing sets 80/20 at random
    # Shuffle dataset before splitting
    X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.2, random_state=42, shuffle=True)

    classifier = svm.SVC(kernel="linear", C=1)
    classifier.fit(X_train, y_train)

    y_pred = classifier.predict(X_test)

    matrix = [ row / np.linalg.norm(row) for row in metrics.confusion_matrix(y_test, y_pred) ]
    self.confusion_matrix(matrix)
    print("")
    print("Model Accuracy: %0.6f" % metrics.accuracy_score(y_test, y_pred))

  def perceptron(self, X, y):
    # Split data into training and testing sets 80/20 at random
    # Shuffle dataset before splitting
    X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.2, random_state=42, shuffle=True)

    classifier = neural_network.MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(1, 1), random_state=1)
    classifier.fit(X_train, y_train)

    y_pred = classifier.predict(X_test)

    matrix = [ row / np.linalg.norm(row) for row in metrics.confusion_matrix(y_test, y_pred) ]
    self.confusion_matrix(matrix)
    print("")
    print("Model Accuracy: %0.6f" % metrics.accuracy_score(y_test, y_pred))

if __name__ == '__main__':
  classifier = Classifier()