from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

class MLIntegrator:
    def split(self, X, y, test_size=0.2):
        return train_test_split(X, y, test_size=test_size)

    def evaluate(self, model, X_test, y_test):
        predictions = model.predict(X_test)
        return accuracy_score(y_test, predictions)
