import numpy as np


class Diagnostics:

    @staticmethod
    def stability_index(data):
        return float(np.std(data) / np.mean(data))

    @staticmethod
    def convergence(samples):
        first_half = np.mean(samples[:len(samples)//2])
        second_half = np.mean(samples[len(samples)//2:])
        return abs(first_half - second_half)
