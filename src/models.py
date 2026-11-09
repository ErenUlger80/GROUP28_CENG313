import numpy as np
from sklearn.dummy import DummyClassifier


def train_dummy(y_train):
    X_train = np.zeros((len(y_train), 1))

    model = DummyClassifier(strategy="prior")
    model.fit(X_train, y_train)

    return model
