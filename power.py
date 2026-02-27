import scipy.stats as stats
import math


class PowerAnalysis:

    @staticmethod
    def solve(effect_size, alpha=0.05, power=0.8):
        z_alpha = stats.norm.ppf(1 - alpha/2)
        z_power = stats.norm.ppf(power)
        n = ((z_alpha + z_power)**2) / (effect_size**2)
        return math.ceil(n)
