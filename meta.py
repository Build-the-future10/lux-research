import numpy as np

class MetaAnalyzer:
    def fixed_effect(self, effect_sizes):
        weights = 1 / np.var(effect_sizes)
        return np.sum(weights * effect_sizes) / np.sum(weights)

    def random_effect(self, effect_sizes):
        return np.mean(effect_sizes)
