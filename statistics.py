import numpy as np
import scipy.stats as stats


class Statistics:

    @staticmethod
    def mean(data):
        return float(np.mean(data))

    @staticmethod
    def variance(data):
        return float(np.var(data, ddof=1))

    @staticmethod
    def confidence_interval(data, confidence=0.95):
        data = np.array(data)
        mean = np.mean(data)
        sem = stats.sem(data)
        margin = sem * stats.t.ppf((1 + confidence) / 2, len(data) - 1)
        return (mean - margin, mean + margin)

    @staticmethod
    def t_test(x, y):
        stat, p = stats.ttest_ind(x, y)
        return {"t_stat": stat, "p_value": p}

    @staticmethod
    def anova(*groups):
        stat, p = stats.f_oneway(*groups)
        return {"f_stat": stat, "p_value": p}

    @staticmethod
    def correlation(x, y):
        r, p = stats.pearsonr(x, y)
        return {"r": r, "p_value": p}
