import numpy as np
from sklearn.linear_model import LinearRegression


class Causal:

    @staticmethod
    def ate(treatment, outcome):
        treatment = np.array(treatment)
        outcome = np.array(outcome)

        treated = outcome[treatment == 1]
        control = outcome[treatment == 0]

        return float(np.mean(treated) - np.mean(control))

    @staticmethod
    def regression_adjustment(X, treatment, outcome):
        X = np.column_stack([X, treatment])
        model = LinearRegression().fit(X, outcome)
        return float(model.coef_[-1])
