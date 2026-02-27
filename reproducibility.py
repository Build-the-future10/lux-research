import numpy as np
import random


class Reproducibility:

    @staticmethod
    def set_seed(seed):
        np.random.seed(seed)
        random.seed(seed)
