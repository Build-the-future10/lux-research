import numpy as np

class DiagnosticSuite:
    def stability_index(self, results):
        return np.std(results) / np.mean(results)

    def complexity_estimate(self, runtime, data_size):
        return runtime / data_size
