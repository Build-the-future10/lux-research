import numpy as np
import scipy.stats as stats

class StatisticalEngine:
    def mean(self, data):
        return np.mean(data)

    def variance(self, data):
        return np.var(data)

    def t_test(self, sample1, sample2):
        return stats.ttest_ind(sample1, sample2)

    def correlation(self, x, y):
        return stats.pearsonr(x, y)

    def regression(self, x, y):
        slope, intercept, r, p, std_err = stats.linregress(x, y)
        return {
            "slope": slope,
            "intercept": intercept,
            "r": r,
            "p": p,
            "std_err": std_err
        }
