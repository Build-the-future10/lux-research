import numpy as np


class BayesianNormal:

    @staticmethod
    def posterior(data, prior_mean=0, prior_var=1):
        data = np.array(data)
        n = len(data)
        sample_mean = np.mean(data)
        sample_var = np.var(data)

        posterior_var = 1 / (n/sample_var + 1/prior_var)
        posterior_mean = posterior_var * (n*sample_mean/sample_var + prior_mean/prior_var)

        return {
            "posterior_mean": float(posterior_mean),
            "posterior_variance": float(posterior_var)
        }
