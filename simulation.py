import numpy as np
from multiprocessing import Pool
from typing import Callable


class MonteCarlo:

    @staticmethod
    def run(model: Callable, n: int = 10000, vectorized=False):
        if vectorized:
            results = model(n)
        else:
            results = np.array([model() for _ in range(n)])

        return MonteCarlo.summary(results)

    @staticmethod
    def parallel(model: Callable, n: int = 10000, processes: int = 4):
        with Pool(processes) as pool:
            results = pool.map(lambda _: model(), range(n))

        return MonteCarlo.summary(np.array(results))

    @staticmethod
    def summary(results):
        return {
            "mean": float(np.mean(results)),
            "std": float(np.std(results)),
            "variance": float(np.var(results)),
            "min": float(np.min(results)),
            "max": float(np.max(results)),
            "n": len(results)
        }
